from fastapi import FastAPI

from backend.app.schemas import AssistantQuery, AssistantResponse, SearchRequest, SearchResponse
from backend.app.services import build_assistant_response, search_documents

app = FastAPI(
    title="Manufacturing Floor Assistant API",
    description="Backend scaffold for the Manufacturing Floor Assistant.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/v1/search", response_model=SearchResponse)
def search(request: SearchRequest) -> SearchResponse:
    return search_documents(
        query=request.query,
        equipment_id=request.equipment_id,
        document_type=request.document_type,
        limit=request.limit,
    )


@app.post("/api/v1/assistant", response_model=AssistantResponse)
def assistant(request: AssistantQuery) -> AssistantResponse:
    return build_assistant_response(
        question=request.question,
        equipment_id=request.equipment_id,
        limit=request.limit,
    )
