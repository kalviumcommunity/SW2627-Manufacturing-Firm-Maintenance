from __future__ import annotations

import re

from fastapi import HTTPException, status

from .data import MACHINE_DATA
from .schemas import (
    AssistantResponse,
    Equipment,
    GuidanceResult,
    GuidanceSource,
    MachineContext,
    MachineSummary,
    SearchResponse,
    SourceExcerpt,
)

STOP_WORDS = {"a", "an", "and", "for", "how", "is", "of", "the", "to", "what", "with"}
SAFETY_TERMS = {"check", "electrical", "guard", "guarding", "inspect", "jam", "lockout", "safety", "service", "stop"}


def list_machines() -> list[MachineSummary]:
    return [
        MachineSummary(machine_id=machine_id, machine_name=payload["machine_name"])
        for machine_id, payload in MACHINE_DATA.items()
    ]


def list_equipment() -> list[Equipment]:
    return [
        Equipment(
            equipment_id=machine_id,
            equipment_name=payload["machine_name"],
            area=payload["area"],
            status=payload["status"],
        )
        for machine_id, payload in MACHINE_DATA.items()
    ]


def get_machine_context(machine_id: str) -> MachineContext:
    payload = MACHINE_DATA.get(machine_id)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unknown machine_id '{machine_id}'",
        )

    return MachineContext(machine_id=machine_id, **payload)


def generate_guidance(machine_id: str, issue: str) -> GuidanceResult:
    context = get_machine_context(machine_id)
    normalized_issue = issue.lower()

    manual_match = next(
        (manual for manual in context.manuals if normalized_issue in manual.title.lower() or normalized_issue in manual.excerpt.lower()),
        context.manuals[0],
    )
    log_match = next(
        (log for log in context.maintenance_logs if normalized_issue in log.issue.lower() or normalized_issue in log.action_taken.lower()),
        context.maintenance_logs[0],
    )
    safety_match = context.safety_procedures[0]

    recommendation = (
        f"Start with '{manual_match.title}'. Then apply recent fix from log '{log_match.id}' "
        f"({log_match.action_taken}). Follow safety procedure '{safety_match.title}' before intervention."
    )

    return GuidanceResult(
        machine_id=machine_id,
        machine_name=context.machine_name,
        issue=issue,
        recommendation=recommendation,
        sources=[
            GuidanceSource(type="manual", id=manual_match.id, title=manual_match.title),
            GuidanceSource(type="maintenance_log", id=log_match.id, title=log_match.issue),
            GuidanceSource(type="safety_procedure", id=safety_match.id, title=safety_match.title),
        ],
    )


def _tokens(text: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9]+", text.lower()) if token not in STOP_WORDS}


def search_sources(
    query: str,
    equipment_id: str | None = None,
    document_type: str | None = None,
    limit: int = 5,
) -> SearchResponse:
    if equipment_id is not None and equipment_id not in MACHINE_DATA:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Unknown equipment_id '{equipment_id}'")

    query_tokens = _tokens(query)
    phrase = query.lower().strip()
    matches: list[SourceExcerpt] = []
    machines = {equipment_id: MACHINE_DATA[equipment_id]} if equipment_id else MACHINE_DATA

    for machine_id, payload in machines.items():
        records = [
            ("manual", item["id"], item["title"], item["section"], item.get("revision", ""), item["excerpt"])
            for item in payload["manuals"]
        ]
        records.extend(
            ("maintenance_log", item["id"], item["issue"], item["section"], item["date"], f"{item['action_taken']} {item['outcome']}")
            for item in payload["maintenance_logs"]
        )
        records.extend(
            ("safety_procedure", item["id"], item["title"], item["section"], item["date"], " ".join(item["steps"]))
            for item in payload["safety_procedures"]
        )

        for kind, record_id, title, section, source_date, content in records:
            if document_type and kind != document_type:
                continue
            haystack = f"{machine_id} {payload['machine_name']} {title} {section} {content}".lower()
            matched_tokens = query_tokens.intersection(_tokens(haystack))
            if not matched_tokens:
                continue
            score = len(matched_tokens) / max(len(query_tokens), 1)
            if phrase in haystack:
                score += 0.35
            if machine_id in phrase or payload["machine_name"].lower() in phrase:
                score += 0.2
            if kind == "safety_procedure" and query_tokens.intersection(SAFETY_TERMS):
                score += 0.25
            matches.append(
                SourceExcerpt(
                    document_id=record_id,
                    document_type=kind,
                    title=title,
                    section=section,
                    source_date=source_date,
                    excerpt=content[:280],
                    score=round(score, 3),
                )
            )

    matches.sort(key=lambda result: (-result.score, result.document_id))
    return SearchResponse(query=query, total=len(matches), results=matches[:limit])


def generate_assistant_response(question: str, equipment_id: str | None, limit: int) -> AssistantResponse:
    search = search_sources(question, equipment_id=equipment_id, limit=limit)
    if not search.results:
        return AssistantResponse(
            answer="No relevant source was found. Do not apply an unverified fix; escalate to a supervisor or maintenance lead.",
            confidence="low",
            sources=[],
        )

    top = search.results[0]
    confidence = "high" if top.score >= 1.0 and len(search.results) > 1 else "medium" if top.score >= 0.45 else "low"
    safety_sources = [source for source in search.results if source.document_type == "safety_procedure"]
    safety_notice = safety_sources[0].excerpt if safety_sources else None
    answer = f"Start with {top.title}: {top.excerpt}"
    if safety_notice:
        answer = f"Follow the safety procedure first. Then {answer[0].lower() + answer[1:]}"
    return AssistantResponse(answer=answer, confidence=confidence, safety_notice=safety_notice, sources=search.results)
