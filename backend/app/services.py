from __future__ import annotations

import re
from typing import Any

from backend.app.data import get_seed_data
from backend.app.schemas import (
    AssistantResponse,
    Confidence,
    SearchRequest,
    SearchResponse,
    SourceExcerpt,
)


def _tokenize(value: str) -> list[str]:
    return [token for token in re.findall(r"[a-z0-9]+", value.lower()) if token]


def _score_match(query: str, text: str) -> float:
    tokens = _tokenize(query)
    if not tokens:
        return 0.0

    normalized_text = text.lower()
    score = 0.0

    if query.lower() in normalized_text:
        score += 2.5

    matched_tokens = 0
    for token in tokens:
        if token in normalized_text:
            matched_tokens += 1
            score += 1.5

    if matched_tokens:
        score += 0.5 * matched_tokens

    return round(score, 4)


def _build_document_candidates() -> list[dict[str, Any]]:
    seed = get_seed_data()
    records: list[dict[str, Any]] = []

    for manual in seed["manuals"]:
        records.append(
            {
                "document_id": manual.document_id,
                "equipment_id": manual.equipment_id,
                "document_type": "manual",
                "title": manual.title,
                "section": manual.section,
                "excerpt": manual.content,
                "content": " ".join(["manual", manual.title, manual.section, manual.content]),
            }
        )

    for log in seed["maintenance_logs"]:
        records.append(
            {
                "document_id": log.document_id,
                "equipment_id": log.equipment_id,
                "document_type": "maintenance_log",
                "title": log.issue,
                "section": "Maintenance log",
                "excerpt": log.action_taken,
                "content": " ".join(["maintenance log", log.issue, log.action_taken, log.outcome]),
            }
        )

    for procedure in seed["safety_procedures"]:
        records.append(
            {
                "document_id": procedure.document_id,
                "equipment_id": procedure.equipment_id,
                "document_type": "safety_procedure",
                "title": procedure.title,
                "section": procedure.section,
                "excerpt": " ".join(procedure.steps),
                "content": " ".join([
                    "safety procedure",
                    procedure.title,
                    procedure.section,
                    *procedure.hazards,
                    *procedure.steps,
                ]),
            }
        )

    return records


def search_documents(
    query: str,
    equipment_id: str | None = None,
    document_type: str | None = None,
    limit: int = 5,
) -> SearchResponse:
    request = SearchRequest(query=query, equipment_id=equipment_id, document_type=document_type, limit=limit)

    matches: list[SourceExcerpt] = []
    for document in _build_document_candidates():
        if request.equipment_id and document["equipment_id"] != request.equipment_id:
            continue
        if request.document_type and document["document_type"] != request.document_type:
            continue

        score = _score_match(request.query, document["content"])
        if score <= 0:
            continue

        excerpt = document["excerpt"]
        if len(excerpt) > 180:
            excerpt = excerpt[:177].rstrip() + "..."

        matches.append(
            SourceExcerpt(
                document_id=document["document_id"],
                equipment_id=document["equipment_id"],
                document_type=document["document_type"],
                title=document["title"],
                section=document["section"],
                excerpt=excerpt,
                score=score,
            )
        )

    matches.sort(key=lambda result: (result.score, result.title), reverse=True)
    return SearchResponse(query=request.query, total=len(matches), results=matches[: request.limit])


def build_assistant_response(
    question: str,
    equipment_id: str | None = None,
    limit: int = 5,
) -> AssistantResponse:
    search_response = search_documents(question, equipment_id=equipment_id, limit=limit)

    if not search_response.results:
        safety_notice = "Follow local lockout/tagout and PPE procedures before inspecting or repairing equipment."
        return AssistantResponse(
            answer="I did not find a matching maintenance or safety record for this issue. Please verify the symptom and equipment state before proceeding.",
            confidence="low",
            safety_notice=safety_notice,
            sources=[],
        )

    top_match = search_response.results[0]
    if top_match.document_type == "manual":
        answer = (
            f"Review the '{top_match.title}' section for this equipment. "
            f"The most relevant guidance states: {top_match.excerpt}"
        )
    elif top_match.document_type == "maintenance_log":
        answer = (
            f"The most recent maintenance record suggests this issue was previously addressed by: "
            f"{top_match.excerpt}"
        )
    else:
        answer = (
            f"Before working on this equipment, follow the '{top_match.title}' procedure. "
            f"Key steps include: {top_match.excerpt}"
        )

    confidence: Confidence = "high" if top_match.score >= 4 else "medium"
    safety_notice = None
    if any(source.document_type == "safety_procedure" for source in search_response.results):
        safety_notice = "Follow lockout/tagout and required PPE before inspecting or repairing this equipment."

    return AssistantResponse(
        answer=answer,
        confidence=confidence,
        safety_notice=safety_notice,
        sources=search_response.results,
    )
