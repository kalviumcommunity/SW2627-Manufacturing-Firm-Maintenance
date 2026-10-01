from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


DocumentType = Literal["manual", "maintenance_log", "safety_procedure"]
EquipmentStatus = Literal["operational", "attention_required", "offline"]
Confidence = Literal["low", "medium", "high"]


class Equipment(BaseModel):
    equipment_id: str = Field(min_length=1)
    equipment_name: str = Field(min_length=1)
    area: str = Field(min_length=1)
    status: EquipmentStatus


class ManualDocument(BaseModel):
    document_id: str = Field(min_length=1)
    equipment_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    revision: str = Field(min_length=1)
    section: str = Field(min_length=1)
    content: str = Field(min_length=1)


class MaintenanceLog(BaseModel):
    document_id: str = Field(min_length=1)
    equipment_id: str = Field(min_length=1)
    occurred_on: date
    issue: str = Field(min_length=1)
    action_taken: str = Field(min_length=1)
    outcome: str = Field(min_length=1)


class SafetyProcedure(BaseModel):
    document_id: str = Field(min_length=1)
    equipment_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    section: str = Field(min_length=1)
    hazards: list[str] = Field(min_length=1)
    required_ppe: list[str] = Field(min_length=1)
    steps: list[str] = Field(min_length=1)


class SourceExcerpt(BaseModel):
    document_id: str = Field(min_length=1)
    equipment_id: str = Field(min_length=1)
    document_type: DocumentType
    title: str = Field(min_length=1)
    section: str = Field(min_length=1)
    excerpt: str = Field(min_length=1)
    score: float = Field(ge=0)


class SearchRequest(BaseModel):
    query: str = Field(min_length=3, max_length=500)
    equipment_id: str | None = Field(default=None, min_length=1)
    document_type: DocumentType | None = None
    limit: int = Field(default=5, ge=1, le=10)


class SearchResponse(BaseModel):
    query: str
    total: int = Field(ge=0)
    results: list[SourceExcerpt]


class AssistantQuery(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    equipment_id: str | None = Field(default=None, min_length=1)
    limit: int = Field(default=5, ge=1, le=10)


class AssistantResponse(BaseModel):
    answer: str = Field(min_length=1)
    confidence: Confidence
    safety_notice: str | None = None
    sources: list[SourceExcerpt]


class ErrorDetail(BaseModel):
    code: str = Field(min_length=1)
    message: str = Field(min_length=1)


class ErrorResponse(BaseModel):
    error: ErrorDetail
