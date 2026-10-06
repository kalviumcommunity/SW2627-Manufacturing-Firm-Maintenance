"use client";
import { useState } from "react";
import Link from "next/link";
import Shell from "../../components/Shell";

const steps = [
  "Stop the press and apply lockout/tagout.",
  "Release stored hydraulic pressure using the bleed valve.",
  "Inspect the main cylinder seal for oil leakage.",
  "Replace the seal kit (part HS-110-K) if worn.",
  "Refill and bleed the system, then run a test cycle at 50% pressure.",
];

export default function Answer() {
  const [vote, setVote] = useState(null);
  const [escalated, setEscalated] = useState(false);

  return (
    <Shell title="Answer detail" topbar={<Link href="/dashboard" className="btn secondary">Back to dashboard</Link>}>
      <div className="split">
        <section className="card">
          <h2>Fix for Error E-47: low system pressure</h2>
          <div className="callout red"><strong>Safety warning:</strong> Relieve pressure before opening any hydraulic line.</div>
          <ol className="steps">{steps.map((s) => <li key={s}>{s}</li>)}</ol>
        </section>
        <section className="card doc">
          <div className="row between">
            <strong>Press 110 Manual, page 84</strong>
            <span className="tag source">Source</span>
          </div>
          <div className="page-preview">
            <h3>8.4 Low pressure fault (E-47)</h3>
            <p>E-47 is raised when system pressure stays below 120 bar for more than 5 seconds during the press cycle.</p>
            <p className="hl">Check the main cylinder seal for leakage. Replace the seal kit if oil is visible on the rod.</p>
            <p>After repair, bleed the circuit and run a test cycle at reduced pressure.</p>
            <div className="line" /><div className="line short" /><div className="line" />
          </div>
        </section>
      </div>
      <div className="card row between mt actions">
        <div className="row">
          <span>Was this helpful?</span>
          <button className={"btn secondary" + (vote === "up" ? " selected-green" : "")} onClick={() => setVote("up")}>👍 Yes</button>
          <button className={"btn secondary" + (vote === "down" ? " selected-red" : "")} onClick={() => setVote("down")}>👎 No</button>
        </div>
        <div className="row">
          {escalated && <span className="tag red">Sent to senior technician</span>}
          <button className="btn amber-outline" onClick={() => setEscalated(true)}>Escalate to senior technician</button>
          <Link href="/dashboard" className="btn primary">Done</Link>
        </div>
      </div>
    </Shell>
  );
}
