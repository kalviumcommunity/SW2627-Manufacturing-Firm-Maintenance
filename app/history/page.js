"use client";
import { useState } from "react";
import Shell, { StatusTag } from "../../components/Shell";
import { logs } from "../../lib/data";

export default function History() {
  const [q, setQ] = useState("");
  const [status, setStatus] = useState("All");
  const rows = logs.filter((l) =>
    (status === "All" || l.status === status) &&
    (l.machine + l.issue + l.resolution).toLowerCase().includes(q.toLowerCase())
  );
  return (
    <Shell title="Machine history">
      <div className="row mb">
        <input className="search light" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Search by machine, issue or resolution" />
        <select value={status} onChange={(e) => setStatus(e.target.value)}>
          {["All", "Resolved", "Pending", "Escalated"].map((s) => <option key={s}>{s}</option>)}
        </select>
      </div>
      <div className="card tablewrap">
        <table>
          <thead><tr><th>Date</th><th>Machine ID</th><th>Issue</th><th>Resolution</th><th>Status</th></tr></thead>
          <tbody>
            {rows.map((l, i) => (
              <tr key={i}><td>{l.date}</td><td><strong>{l.machine}</strong></td><td>{l.issue}</td><td>{l.resolution}</td><td><StatusTag status={l.status} /></td></tr>
            ))}
            {rows.length === 0 && <tr><td colSpan={5} className="muted center">No logs match. Try clearing the filters.</td></tr>}
          </tbody>
        </table>
      </div>
    </Shell>
  );
}
