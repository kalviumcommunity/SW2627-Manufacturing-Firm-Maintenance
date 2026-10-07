import Link from "next/link";
import Shell from "../../../components/Shell";
import { failures, fixTrend, lowRated } from "../../../lib/data";

export default function Analytics() {
  const max = Math.max(...failures.map((f) => f.count));
  const w = 520, h = 180, lo = Math.min(...fixTrend) - 5, hi = Math.max(...fixTrend) + 5;
  const pts = fixTrend.map((v, i) => [20 + (i * (w - 40)) / (fixTrend.length - 1), h - 20 - ((v - lo) / (hi - lo)) * (h - 40)]);
  const line = pts.map((p) => p.join(",")).join(" ");
  return (
    <Shell role="admin" title="Feedback and analytics" topbar={<Link href="/admin" className="btn secondary">Back to admin dashboard</Link>}>
      <div className="grid2">
        <section className="card">
          <h2>Most frequent machine failures</h2>
          {failures.map((f) => (
            <div className="bar-row" key={f.name}>
              <span className="bar-label">{f.name}</span>
              <div className="bar"><div style={{ width: (f.count / max) * 100 + "%" }} /></div>
              <strong>{f.count}</strong>
            </div>
          ))}
        </section>
        <section className="card">
          <h2>Average time-to-fix (minutes, last 7 weeks)</h2>
          <svg viewBox={`0 0 ${w} ${h}`} width="100%" role="img" aria-label="Time to fix trend">
            <polyline points={line} fill="none" stroke="#F2A623" strokeWidth="3" />
            {pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r="5" fill="#0F1B2E" />)}
            {pts.map((p, i) => <text key={i} x={p[0]} y={p[1] - 10} fontSize="12" textAnchor="middle" fill="#0F1B2E">{fixTrend[i]}</text>)}
          </svg>
        </section>
      </div>
      <h2 className="mt">Low-rated answers to review</h2>
      <div className="card list">
        {lowRated.map((l) => (
          <div className="list-item" key={l.q}>
            <div><strong>{l.q}</strong><div className="muted small">{l.machine} · {l.note}</div></div>
            <div className="row"><span className="tag red">{l.rating}</span><button className="btn secondary sm">Review</button></div>
          </div>
        ))}
      </div>
    </Shell>
  );
}
