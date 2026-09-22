from datetime import date

import pytest
from pydantic import ValidationError

from backend.app.schemas import (
    AssistantQuery,
    Equipment,
    ErrorResponse,
    MaintenanceLog,
    ManualDocument,
    SafetyProcedure,
    SearchRequest,
    SourceExcerpt,
)


def test_equipment_schema_accepts_supported_status() -> None:
    equipment = Equipment(
        equipment_id="conveyor-01",
        equipment_name="Assembly Conveyor Charlie",
        area="Assembly",
        status="operational",
    )

    assert equipment.equipment_id == "conveyor-01"


def test_manual_and_maintenance_schemas_preserve_source_fields() -> None:
    manual = ManualDocument(
        document_id="manual-001",
        equipment_id="conveyor-01",
        title="Motor temperature",
        revision="Rev 1",
        section="Troubleshooting",
        content="Check airflow and belt tension.",
    )
    log = MaintenanceLog(
        document_id="log-001",
        equipment_id="conveyor-01",
        occurred_on=date(2026, 9, 21),
        issue="Motor overheating",
        action_taken="Cleared the cooling screen.",
        outcome="Temperature returned to normal.",
    )

    assert manual.revision == "Rev 1"
    assert log.occurred_on == date(2026, 9, 21)


def test_safety_procedure_requires_hazard_ppe_and_steps() -> None:
    procedure = SafetyProcedure(
        document_id="safety-001",
        equipment_id="conveyor-01",
        title="Conveyor lockout",
        section="Energy isolation",
        hazards=["Stored electrical energy"],
        required_ppe=["Eye protection"],
        steps=["Apply lockout/tagout.", "Verify zero energy."],
    )

    assert procedure.required_ppe == ["Eye protection"]


def test_search_request_defaults_and_bounds() -> None:
    request = SearchRequest(query="motor overheating")

    assert request.limit == 5
    assert request.document_type is None

    with pytest.raises(ValidationError):
        SearchRequest(query="motor", limit=0)
    with pytest.raises(ValidationError):
        SearchRequest(query="motor", limit=11)
    with pytest.raises(ValidationError):
        SearchRequest(query="no")


def test_document_type_is_restricted_to_contract_values() -> None:
    with pytest.raises(ValidationError):
        SearchRequest(query="motor overheating", document_type="unknown")


def test_assistant_query_has_bounded_question_and_limit() -> None:
    query = AssistantQuery(question="What should I check?", equipment_id="press-02", limit=3)

    assert query.equipment_id == "press-02"
    assert query.limit == 3

    with pytest.raises(ValidationError):
        AssistantQuery(question="x" * 501)


def test_source_excerpt_requires_non_negative_score() -> None:
    with pytest.raises(ValidationError):
        SourceExcerpt(
            document_id="manual-001",
            equipment_id="conveyor-01",
            document_type="manual",
            title="Motor temperature",
            section="Troubleshooting",
            excerpt="Check airflow.",
            score=-0.1,
        )


def test_error_response_has_stable_nested_shape() -> None:
    error = ErrorResponse.model_validate(
        {"error": {"code": "invalid_query", "message": "Query is too short."}}
    )

    assert error.error.code == "invalid_query"
