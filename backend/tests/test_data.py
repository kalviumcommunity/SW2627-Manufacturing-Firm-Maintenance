from backend.app.data import get_seed_data, get_equipment_by_id


def test_seed_data_contains_machine_catalog_and_sources() -> None:
    seed = get_seed_data()

    assert [machine.equipment_id for machine in seed["equipment"]] == [
        "conveyor-01",
        "press-02",
        "mixer-03",
    ]
    assert seed["manuals"][0].equipment_id == "conveyor-01"
    assert any(doc.title == "Conveyor belt tension adjustment" for doc in seed["manuals"])
    assert seed["maintenance_logs"][0].equipment_id == "conveyor-01"
    assert seed["safety_procedures"][0].equipment_id == "conveyor-01"


def test_get_equipment_by_id_returns_the_requested_machine() -> None:
    machine = get_equipment_by_id("press-02")

    assert machine is not None
    assert machine.equipment_name == "Hydraulic Press B"
    assert machine.area == "Stamping"
