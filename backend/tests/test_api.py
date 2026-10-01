from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_search_route_returns_ranked_source_results() -> None:
    response = client.post(
        "/api/v1/search",
        json={"query": "belt tension", "equipment_id": "conveyor-01", "limit": 3},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["query"] == "belt tension"
    assert payload["total"] >= 1
    assert payload["results"][0]["document_id"] == "manual-001"


def test_assistant_route_returns_source_referenced_guidance() -> None:
    response = client.post(
        "/api/v1/assistant",
        json={"question": "Why is the conveyor belt slipping?", "equipment_id": "conveyor-01"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["confidence"] in {"medium", "high"}
    assert payload["sources"]
    assert "conveyor" in payload["answer"].lower()


def test_routes_return_fastapi_validation_errors_for_invalid_requests() -> None:
    response = client.post("/api/v1/search", json={"query": "no"})

    assert response.status_code == 422
    assert response.json()["detail"]


def test_unknown_equipment_is_valid_but_returns_no_matches() -> None:
    response = client.post(
        "/api/v1/search",
        json={"query": "motor issue", "equipment_id": "unknown-99"},
    )

    assert response.status_code == 200
    assert response.json()["total"] == 0
    assert response.json()["results"] == []
