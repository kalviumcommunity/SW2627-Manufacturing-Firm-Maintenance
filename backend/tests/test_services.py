from backend.app.services import build_assistant_response, search_documents


def test_search_documents_prioritizes_machine_specific_matches() -> None:
    results = search_documents("belt tension", equipment_id="conveyor-01", limit=3)

    assert results.total >= 1
    assert results.results[0].equipment_id == "conveyor-01"
    assert results.results[0].title == "Conveyor belt tension adjustment"
    assert results.results[0].score > 0


def test_search_documents_filters_by_document_type() -> None:
    results = search_documents("safety", document_type="safety_procedure", limit=5)

    assert results.total >= 1
    assert all(result.document_type == "safety_procedure" for result in results.results)


def test_build_assistant_response_uses_best_match_and_safety_notice() -> None:
    response = build_assistant_response("belt slipping on conveyor", equipment_id="conveyor-01", limit=3)

    assert response.confidence in {"medium", "high"}
    assert response.sources
    assert "lockout" in response.safety_notice.lower() or response.safety_notice is None
