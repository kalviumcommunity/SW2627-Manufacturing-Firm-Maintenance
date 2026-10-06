"use client";
import { useState, useRef, useEffect } from "react";
import Link from "next/link";
import Shell from "../../components/Shell";

const first = [
  { from: "user", text: "Error E-47 on hydraulic press 110. Pressure keeps dropping during the cycle." },
  {
    from: "ai",
    text: "E-47 indicates low system pressure. Start with the checks below.",
    steps: ["Stop the machine and release stored pressure.", "Inspect the main cylinder seal for leaks.", "Check the pump relief valve setting."],
    warning: "Lock out and tag out the press and relieve hydraulic pressure before opening any line.",
    sources: ["Press 110 Manual, p. 84", "Maintenance Log, 12 Mar 2026"],
  },
];

export default function Chat() {
  const [msgs, setMsgs] = useState(first);
  const [text, setText] = useState("");
  const [listening, setListening] = useState(false);
  const end = useRef(null);
  useEffect(() => { end.current && end.current.scrollIntoView({ behavior: "smooth" }); }, [msgs]);

  const send = () => {
    if (!text.trim()) return;
    const t = text.trim();
    setText("");
    setMsgs((m) => [...m, { from: "user", text: t }]);
    setTimeout(() => {
      setMsgs((m) => [...m, {
        from: "ai",
        text: "Based on the manuals and past logs, check the sensor wiring and recalibrate. Tell me the machine ID for exact steps.",
        sources: ["Operator Guide, p. 22"],
      }]);
    }, 700);
  };

  return (
    <Shell title="Ask AI" topbar={<Link href="/dashboard" className="btn secondary">Back to dashboard</Link>}>
      <div className="chat">
        <div className="chat-scroll">
          {msgs.map((m, i) => (
            <div key={i} className={"bubble-row " + m.from}>
              <div className={"bubble " + m.from}>
                <p>{m.text}</p>
                {m.steps && <ol>{m.steps.map((s) => <li key={s}>{s}</li>)}</ol>}
                {m.warning && <div className="callout red"><strong>Safety warning:</strong> {m.warning}</div>}
                {m.sources && (
                  <div className="sources">
                    {m.sources.map((s) => <span className="tag source" key={s}>Source: {s}</span>)}
                  </div>
                )}
                {m.steps && <Link href="/answer" className="btn primary sm mt-s">View full answer</Link>}
              </div>
            </div>
          ))}
          <div ref={end} />
        </div>
        <div className="composer">
          <button className={"icon-btn" + (listening ? " live" : "")} onClick={() => setListening(!listening)} aria-label="Voice input">🎤</button>
          <input value={text} onChange={(e) => setText(e.target.value)} onKeyDown={(e) => e.key === "Enter" && send()} placeholder={listening ? "Listening..." : "Describe the issue or enter error code..."} />
          <button className="btn primary" onClick={send}>Send</button>
        </div>
      </div>
    </Shell>
  );
}
