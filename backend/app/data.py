from __future__ import annotations

from typing import Any

from backend.app.schemas import (
    Equipment,
    MaintenanceLog,
    ManualDocument,
    SafetyProcedure,
)


def get_seed_data() -> dict[str, list[Any]]:
    equipment = [
        Equipment(
            equipment_id="conveyor-01",
            equipment_name="Assembly Conveyor Charlie",
            area="Assembly",
            status="operational",
        ),
        Equipment(
            equipment_id="press-02",
            equipment_name="Hydraulic Press B",
            area="Stamping",
            status="attention_required",
        ),
        Equipment(
            equipment_id="mixer-03",
            equipment_name="Batch Mixer 3",
            area="Mixing",
            status="offline",
        ),
    ]

    manuals = [
        ManualDocument(
            document_id="manual-001",
            equipment_id="conveyor-01",
            title="Conveyor belt tension adjustment",
            revision="Rev 4",
            section="Troubleshooting",
            content=(
                "If the conveyor is slipping, inspect the belt tension and verify the drive "
                "alignment before adjusting the tensioner. Check for debris on the drive rollers "
                "and confirm the motor current is within the normal operating range."
            ),
        ),
        ManualDocument(
            document_id="manual-002",
            equipment_id="press-02",
            title="Hydraulic press ram alignment",
            revision="Rev 2",
            section="Calibration",
            content=(
                "When the ram is not centered, inspect the tie-bars for even extension and verify "
                "the die set is seated fully before re-running the press at half load."
            ),
        ),
        ManualDocument(
            document_id="manual-003",
            equipment_id="mixer-03",
            title="Mixer shaft bearing inspection",
            revision="Rev 1",
            section="Preventive maintenance",
            content=(
                "Listen for abnormal bearing noise and check for heat on the shaft bearing housing. "
                "If the shaft drifts, inspect the coupling and re-torque the mounting hardware."
            ),
        ),
    ]

    maintenance_logs = [
        MaintenanceLog(
            document_id="log-001",
            equipment_id="conveyor-01",
            occurred_on="2026-09-18",
            issue="Drive belt was slipping during a heavy load cycle.",
            action_taken="Cleaned the drive rollers and re-tensioned the belt to spec.",
            outcome="Conveyor returned to stable operation for the next three shifts.",
        ),
        MaintenanceLog(
            document_id="log-002",
            equipment_id="press-02",
            occurred_on="2026-09-20",
            issue="Press ram was drifting left during the final quarter of the stroke.",
            action_taken="Realigned the die and checked the hydraulic pressure balance.",
            outcome="Cycle consistency improved and the machine cleared quality inspection.",
        ),
        MaintenanceLog(
            document_id="log-003",
            equipment_id="mixer-03",
            occurred_on="2026-09-17",
            issue="Mixer shaft showed elevated vibration at startup.",
            action_taken="Inspected the coupling and replaced a worn bearing housing seal.",
            outcome="Vibration dropped below the warning threshold and the unit was returned to service.",
        ),
    ]

    safety_procedures = [
        SafetyProcedure(
            document_id="safety-001",
            equipment_id="conveyor-01",
            title="Conveyor lockout and restart",
            section="Energy isolation",
            hazards=["Stored mechanical energy", "Pinch points"],
            required_ppe=["Safety glasses", "Cut-resistant gloves"],
            steps=[
                "Stop the conveyor and notify the nearby operators.",
                "Apply lockout/tagout to the main disconnect and verify zero energy.",
                "Inspect the belt and guard before restarting the line."
            ],
        ),
        SafetyProcedure(
            document_id="safety-002",
            equipment_id="press-02",
            title="Hydraulic press safe setup",
            section="Setup and tooling",
            hazards=["Crushing hazard", "High-pressure fluid leak"],
            required_ppe=["Face shield", "Safety glasses", "Steel-toe boots"],
            steps=[
                "Confirm the tooling is seated and the work area is clear.",
                "Use the guarded controls only and keep hands clear of the descent path.",
                "Perform a dry cycle and inspect for leaks before full production use."
            ],
        ),
        SafetyProcedure(
            document_id="safety-003",
            equipment_id="mixer-03",
            title="Mixer guard inspection",
            section="Before startup",
            hazards=["Rotating shaft", "Splash hazard"],
            required_ppe=["Safety glasses", "Chemical-resistant gloves"],
            steps=[
                "Check that all guards are in place and interlocks are functioning.",
                "Verify the mixer bowl is secured and the material feed is clear.",
                "Inspect for leaks and then start the mixer at low speed."
            ],
        ),
    ]

    return {
        "equipment": equipment,
        "manuals": manuals,
        "maintenance_logs": maintenance_logs,
        "safety_procedures": safety_procedures,
    }


def get_equipment_by_id(equipment_id: str) -> Equipment | None:
    for equipment in get_seed_data()["equipment"]:
        if equipment.equipment_id == equipment_id:
            return equipment
    return None
