from __future__ import annotations

MACHINE_DATA = {
    "cnc-01": {
        "machine_name": "CNC Mill Alpha",
        "area": "Precision Machining",
        "status": "attention_required",
        "manuals": [
            {
                "id": "M-100",
                "title": "Spindle Overheat Troubleshooting",
                "section": "Overheating",
                "revision": "Rev 3",
                "excerpt": "If spindle temperature exceeds 85C, stop operation, check coolant line flow, and inspect spindle fan.",
            },
            {
                "id": "M-101",
                "title": "Axis Calibration Procedure",
                "section": "Calibration",
                "revision": "Rev 2",
                "excerpt": "Run axis calibration macro after replacing belts or after vibration alarms.",
            },
        ],
        "maintenance_logs": [
            {
                "id": "L-501",
                "date": "2026-08-29",
                "section": "Corrective maintenance",
                "issue": "Spindle vibration alarm",
                "action_taken": "Replaced spindle fan and cleared debris from coolant inlet.",
                "outcome": "Alarm frequency reduced.",
            },
            {
                "id": "L-507",
                "date": "2026-09-11",
                "section": "Corrective maintenance",
                "issue": "Recurring spindle overheat",
                "action_taken": "Coolant flow restored by replacing clogged filter cartridge.",
                "outcome": "Temperature stabilized below threshold.",
            },
        ],
        "safety_procedures": [
            {
                "id": "S-210",
                "title": "Lockout Before Spindle Service",
                "section": "Energy isolation",
                "date": "2026-01-15",
                "steps": [
                    "Power down machine from main panel.",
                    "Apply lockout/tagout device.",
                    "Verify zero energy state before opening spindle housing.",
                ],
            }
        ],
    },
    "press-02": {
        "machine_name": "Hydraulic Press Bravo",
        "area": "Forming",
        "status": "operational",
        "manuals": [
            {
                "id": "M-220",
                "title": "Hydraulic Pressure Drop Recovery",
                "section": "Pressure loss",
                "revision": "Rev 1",
                "excerpt": "Check reservoir levels, inspect suction line for leaks, and verify pump motor current.",
            }
        ],
        "maintenance_logs": [
            {
                "id": "L-610",
                "date": "2026-09-02",
                "section": "Corrective maintenance",
                "issue": "Slow ram movement",
                "action_taken": "Refilled hydraulic fluid and tightened suction connector.",
                "outcome": "Cycle time restored to baseline.",
            }
        ],
        "safety_procedures": [
            {
                "id": "S-330",
                "title": "Press Jam Clearance",
                "section": "Guarding and jam clearance",
                "date": "2026-02-10",
                "steps": [
                    "Engage emergency stop.",
                    "Use approved clearance tool; never use hands near die area.",
                    "Restart only after supervisor verification.",
                ],
            }
        ],
    },
    "conveyor-01": {
        "machine_name": "Assembly Conveyor Charlie",
        "area": "Assembly",
        "status": "operational",
        "manuals": [
            {
                "id": "M-310",
                "title": "Conveyor Motor Overheating",
                "section": "Motor temperature",
                "revision": "Rev 4",
                "excerpt": "Stop the conveyor and check airflow, bearing temperature, belt tension, and overload indicators.",
            }
        ],
        "maintenance_logs": [
            {
                "id": "L-711",
                "date": "2026-09-08",
                "section": "Corrective maintenance",
                "issue": "Motor overheating and belt slip",
                "action_taken": "Adjusted belt tension and replaced a blocked cooling screen.",
                "outcome": "Motor temperature returned to normal range.",
            }
        ],
        "safety_procedures": [
            {
                "id": "S-410",
                "title": "Conveyor Lockout and Guarding",
                "section": "Energy isolation",
                "date": "2026-03-01",
                "steps": [
                    "Stop the conveyor and isolate electrical energy.",
                    "Apply lockout/tagout before removing a guard.",
                    "Wear eye protection and keep hands clear of pinch points.",
                ],
            }
        ],
    },
}
