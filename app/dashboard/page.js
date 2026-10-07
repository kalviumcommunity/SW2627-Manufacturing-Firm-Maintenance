"use client";
import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import Shell, { StatusTag } from "../../components/Shell";
import { machines, recentQueries } from "../../lib/data";

export default function Dashboard() {
  const router = useRouter();
  const [q, setQ] = useState("");
  const [showAlert, setShowAlert] = useState(true);

  const topbar = (
    <input
      className="search"
      value={q}
      onChange={(e) => setQ(e.target.value)}
      onKeyDown={(e) => e.key === "Enter" && router.push("/chat")}
      placeholder="Describe the issue or enter error code..."
    />
  );

  return (
    <Shell title="Home" topbar={topbar}>
      {showAlert && (
        <div className="banner red">
          <strong>Safety alert:</strong> Hydraulic Press 110 is in fault. Lock out and tag out before any inspection.
          <button className="btn ghost sm" onClick={() => setShowAlert(false)}>Dismiss</button>
        </div>
      )}
      <h2>Quick access machines</h2>
      <div className="grid3">
        {machines.map((m) => (
          <Link href="/chat" key={m.id} className="card hover machine">
            <div className="row between"><strong>{m.id}</strong><StatusTag status={m.status} /></div>
            <p className="muted">{m.name}</p>
            <span className="small amber-text">Ask about this machine</span>
          </Link>
        ))}
      </div>
      <div className="row between mt">
        <h2>Recent queries</h2>
        <Link href="/history" className="btn secondary">View machine history</Link>
      </div>
      <div className="card list">
        {recentQueries.map((r) => (
          <Link href="/answer" key={r.q} className="list-item">
            <div><strong>{r.q}</strong><div className="muted small">{r.machine} · {r.time}</div></div>
            <StatusTag status={r.status} />
          </Link>
        ))}
      </div>
    </Shell>
  );
}
