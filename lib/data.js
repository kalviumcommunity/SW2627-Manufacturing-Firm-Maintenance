export const machines = [
  { id: "CNC-204", name: "CNC Lathe 204", status: "Running" },
  { id: "PRS-110", name: "Hydraulic Press 110", status: "Fault" },
  { id: "CNV-017", name: "Conveyor Line 17", status: "Running" },
  { id: "WLD-052", name: "Welding Robot 52", status: "Maintenance" },
  { id: "CMP-009", name: "Air Compressor 9", status: "Running" },
  { id: "PKG-301", name: "Packaging Unit 301", status: "Running" },
];

export const recentQueries = [
  { q: "Error E-47 on hydraulic press, pressure drops", machine: "PRS-110", time: "12 min ago", status: "Pending" },
  { q: "Conveyor belt slipping at tail pulley", machine: "CNV-017", time: "Yesterday", status: "Resolved" },
  { q: "Spindle overheating on CNC lathe", machine: "CNC-204", time: "2 days ago", status: "Resolved" },
  { q: "Welding robot arm not homing", machine: "WLD-052", time: "3 days ago", status: "Escalated" },
];

export const logs = [
  { date: "2026-10-04", machine: "PRS-110", issue: "Error E-47, pressure drop", resolution: "Replaced hydraulic seal kit", status: "Resolved" },
  { date: "2026-10-03", machine: "WLD-052", issue: "Arm not homing", resolution: "Awaiting senior review", status: "Escalated" },
  { date: "2026-10-02", machine: "CNV-017", issue: "Belt slipping", resolution: "Tension adjusted, pulley cleaned", status: "Resolved" },
  { date: "2026-10-01", machine: "CNC-204", issue: "Spindle overheating", resolution: "Coolant flushed and refilled", status: "Resolved" },
  { date: "2026-09-29", machine: "CMP-009", issue: "Unusual vibration", resolution: "Part ordered: mount bracket", status: "Pending" },
  { date: "2026-09-27", machine: "PKG-301", issue: "Sensor misread on line", resolution: "Sensor recalibrated", status: "Resolved" },
  { date: "2026-09-25", machine: "PRS-110", issue: "Slow ram return", resolution: "Pending valve inspection", status: "Pending" },
];

export const documents = [
  { id: 1, name: "Hydraulic Press 110 Service Manual", type: "Manual", date: "2026-09-30", status: "Processed" },
  { id: 2, name: "CNC Lathe 204 Operator Guide", type: "Manual", date: "2026-09-28", status: "Processed" },
  { id: 3, name: "Maintenance Log Q3 2026", type: "Log", date: "2026-10-01", status: "Processing" },
  { id: 4, name: "Lockout/Tagout Procedure", type: "Safety", date: "2026-09-12", status: "Processed" },
  { id: 5, name: "Welding Robot 52 Troubleshooting", type: "Manual", date: "2026-10-03", status: "Failed" },
  { id: 6, name: "Confined Space Entry Safety", type: "Safety", date: "2026-08-20", status: "Processed" },
];

export const failures = [
  { name: "PRS-110", count: 42 }, { name: "CNV-017", count: 31 },
  { name: "WLD-052", count: 26 }, { name: "CNC-204", count: 19 }, { name: "CMP-009", count: 11 },
];

export const fixTrend = [48, 44, 41, 39, 35, 33, 29];

export const lowRated = [
  { q: "Error E-47 on press, pressure drops", rating: "1/5", note: "Steps skipped the pressure relief check", machine: "PRS-110" },
  { q: "Robot arm homing fails", rating: "2/5", note: "Cited the wrong manual revision", machine: "WLD-052" },
  { q: "Compressor vibration at startup", rating: "2/5", note: "No source page was shown", machine: "CMP-009" },
];
