from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_health_route_reports_service_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_equipment_route_returns_machine_catalogue() -> None:
    response = client.get("/api/v1/equipment")

    assert response.status_code == 200
    payload = response.json()
    assert [machine["equipment_id"] for machine in payload] == [
        "conveyor-01",
        "press-02",
        "mixer-03",
    ]


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


def test_search_route_filters_results_by_document_type() -> None:
    response = client.post(
        "/api/v1/search",
        json={"query": "safety", "document_type": "safety_procedure"},
    )

    assert response.status_code == 200
    assert response.json()["total"] >= 1
    assert all(
        result["document_type"] == "safety_procedure"
        for result in response.json()["results"]
    )


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


def test_assistant_route_returns_safe_fallback_when_no_source_matches() -> None:
    response = client.post(
        "/api/v1/assistant",
        json={"question": "unrecognized thermal anomaly", "equipment_id": "press-02"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["confidence"] == "low"
    assert payload["sources"] == []
    assert "lockout" in payload["safety_notice"].lower()


def test_routes_return_fastapi_validation_errors_for_invalid_requests() -> None:
    response = client.post("/api/v1/search", json={"query": "no"})

    assert response.status_code == 422
    assert response.json()["detail"]


def test_openapi_documents_day_five_operations() -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    paths = response.json()["paths"]
    assert "get" in paths["/api/v1/equipment"]
    assert "post" in paths["/api/v1/search"]
    assert "post" in paths["/api/v1/assistant"]


def test_api_allows_frontend_origin_for_development() -> None:
    response = client.options(
        "/api/v1/equipment",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
        },
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"


def test_unknown_equipment_is_valid_but_returns_no_matches() -> None:
    response = client.post(
        "/api/v1/search",
        json={"query": "motor issue", "equipment_id": "unknown-99"},
    )

    assert response.status_code == 200
    assert response.json()["total"] == 0
    assert response.json()["results"] == []
