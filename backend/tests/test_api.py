from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "0.1.0"}


def test_equipment_list_contains_seeded_machines() -> None:
    response = client.get("/api/v1/equipment")

    assert response.status_code == 200
    assert {item["equipment_id"] for item in response.json()} == {
        "cnc-01",
        "press-02",
        "conveyor-01",
    }


def test_unknown_equipment_returns_not_found() -> None:
    response = client.get("/api/v1/equipment/unknown-99")

    assert response.status_code == 404


def test_search_returns_ranked_source_metadata() -> None:
    response = client.get("/api/v1/search", params={"q": "conveyor motor overheating"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["total"] >= 1
    assert payload["results"][0]["document_id"] == "M-310"
    assert payload["results"][0]["document_type"] == "manual"
    assert payload["results"][0]["section"] == "Motor temperature"


def test_search_can_filter_by_document_type() -> None:
    response = client.get(
        "/api/v1/search",
        params={"q": "lockout conveyor", "document_type": "safety_procedure"},
    )

    assert response.status_code == 200
    assert response.json()["results"]
    assert all(item["document_type"] == "safety_procedure" for item in response.json()["results"])


def test_assistant_prioritizes_safety_sources() -> None:
    response = client.post(
        "/api/v1/assistant/query",
        json={"question": "How do I inspect the conveyor guard?", "equipment_id": "conveyor-01"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["sources"]
    assert payload["safety_notice"]
    assert "safety procedure" in payload["answer"].lower()


def test_assistant_does_not_invent_no_match_fix() -> None:
    response = client.post(
        "/api/v1/assistant/query",
        json={"question": "robotic welding coolant failure", "equipment_id": "conveyor-01"},
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["confidence"] == "low"
    assert payload["sources"] == []
    assert "no relevant source" in payload["answer"].lower()


def test_query_validation_rejects_short_questions() -> None:
    response = client.get("/api/v1/search", params={"q": "no"})

    assert response.status_code == 422


def test_frontend_origin_is_allowed_by_cors() -> None:
    response = client.get(
        "/api/v1/health",
        headers={"Origin": "http://localhost:3000"},
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"
