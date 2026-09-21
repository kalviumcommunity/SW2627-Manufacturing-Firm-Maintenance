from __future__ import annotations

import os

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from .schemas import (
    AssistantQuery,
    AssistantResponse,
    Equipment,
    GuidanceRequest,
    GuidanceResult,
    HealthResponse,
    MachineContext,
    MachineSummary,
    SearchResponse,
)
from .services import (
    generate_assistant_response,
    generate_guidance,
    get_machine_context,
    list_equipment,
    list_machines,
    search_sources,
)

app = FastAPI(
    title="Manufacturing Floor Assistant API",
    description="Backend service for machine troubleshooting using simulated manuals, logs, and safety procedures.",
    version="0.1.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_ORIGIN", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/v1/health", response_model=HealthResponse)
def api_health() -> HealthResponse:
    return HealthResponse(status="ok", version=app.version)


@app.get("/machines", response_model=list[MachineSummary])
def get_machines() -> list[MachineSummary]:
    return list_machines()


@app.get("/machines/{machine_id}", response_model=MachineContext)
def get_machine(machine_id: str) -> MachineContext:
    return get_machine_context(machine_id)


@app.post("/guidance", response_model=GuidanceResult)
def get_guidance(payload: GuidanceRequest) -> GuidanceResult:
    return generate_guidance(machine_id=payload.machine_id, issue=payload.issue)


@app.get("/api/v1/equipment", response_model=list[Equipment])
def get_equipment() -> list[Equipment]:
    return list_equipment()


@app.get("/api/v1/equipment/{equipment_id}", response_model=MachineContext)
def get_equipment_context(equipment_id: str) -> MachineContext:
    return get_machine_context(equipment_id)


@app.get("/api/v1/search", response_model=SearchResponse)
def search(
    q: str = Query(min_length=3, max_length=500),
    equipment_id: str | None = Query(default=None),
    document_type: str | None = Query(default=None),
    limit: int = Query(default=5, ge=1, le=10),
) -> SearchResponse:
    return search_sources(q, equipment_id=equipment_id, document_type=document_type, limit=limit)


@app.post("/api/v1/assistant/query", response_model=AssistantResponse)
def assistant_query(payload: AssistantQuery) -> AssistantResponse:
    return generate_assistant_response(
        question=payload.question,
        equipment_id=payload.equipment_id,
        limit=payload.limit,
    )
