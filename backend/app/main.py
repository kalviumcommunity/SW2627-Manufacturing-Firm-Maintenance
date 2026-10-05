from fastapi import FastAPI

from backend.app.schemas import AssistantQuery, AssistantResponse, SearchRequest, SearchResponse
from backend.app.services import build_assistant_response, search_documents

app = FastAPI(
    title="Manufacturing Floor Assistant API",
    description="Backend scaffold for the Manufacturing Floor Assistant.",
    version="0.1.0",
    openapi_tags=[
        {"name": "system", "description": "Service availability checks."},
        {"name": "troubleshooting", "description": "Source-grounded machine troubleshooting."},
    ],
)


@app.get(
    "/health",
    tags=["system"],
    summary="Check service health",
    operation_id="getHealth",
)
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/api/v1/search",
    response_model=SearchResponse,
    tags=["troubleshooting"],
    summary="Search troubleshooting sources",
    operation_id="searchSources",
)
def search(request: SearchRequest) -> SearchResponse:
    return search_documents(
        query=request.query,
        equipment_id=request.equipment_id,
        document_type=request.document_type,
        limit=request.limit,
    )


@app.post(
    "/api/v1/assistant",
    response_model=AssistantResponse,
    tags=["troubleshooting"],
    summary="Get source-referenced troubleshooting guidance",
    operation_id="getAssistantGuidance",
)
def assistant(request: AssistantQuery) -> AssistantResponse:
    return build_assistant_response(
        question=request.question,
        equipment_id=request.equipment_id,
        limit=request.limit,
    )
