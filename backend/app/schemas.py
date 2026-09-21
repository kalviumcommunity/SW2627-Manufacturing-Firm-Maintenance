from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

DocumentType = Literal["manual", "maintenance_log", "safety_procedure"]


class ManualEntry(BaseModel):
    id: str
    title: str
    excerpt: str


class MaintenanceLogEntry(BaseModel):
    id: str
    date: str
    issue: str
    action_taken: str
    outcome: str


class SafetyProcedure(BaseModel):
    id: str
    title: str
    steps: list[str]


class MachineSummary(BaseModel):
    machine_id: str
    machine_name: str


class MachineContext(BaseModel):
    machine_id: str
    machine_name: str
    manuals: list[ManualEntry]
    maintenance_logs: list[MaintenanceLogEntry]
    safety_procedures: list[SafetyProcedure]


class GuidanceSource(BaseModel):
    type: Literal["manual", "maintenance_log", "safety_procedure"]
    id: str
    title: str


class GuidanceResult(BaseModel):
    machine_id: str
    machine_name: str
    issue: str
    recommendation: str
    sources: list[GuidanceSource]


class GuidanceRequest(BaseModel):
    machine_id: str = Field(min_length=1)
    issue: str = Field(min_length=3)


class Equipment(BaseModel):
    equipment_id: str
    equipment_name: str
    area: str
    status: Literal["operational", "attention_required", "offline"]


class SourceExcerpt(BaseModel):
    document_id: str
    document_type: DocumentType
    title: str
    section: str
    source_date: str
    excerpt: str
    score: float = Field(ge=0)


class SearchResponse(BaseModel):
    query: str
    total: int
    results: list[SourceExcerpt]


class AssistantQuery(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    equipment_id: str | None = Field(default=None, min_length=1)
    limit: int = Field(default=5, ge=1, le=10)


class AssistantResponse(BaseModel):
    answer: str
    confidence: Literal["low", "medium", "high"]
    safety_notice: str | None = None
    sources: list[SourceExcerpt]


class HealthResponse(BaseModel):
    status: Literal["ok"]
    version: str
