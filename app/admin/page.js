"use client";
import { useState } from "react";
import Link from "next/link";
import Shell, { StatusTag } from "../../components/Shell";
import { documents } from "../../lib/data";

export default function Admin() {
  const [docs, setDocs] = useState(documents.slice(0, 4));
  const [over, setOver] = useState(false);
  const add = (files) => {
    const added = Array.from(files).map((f, i) => ({ id: Date.now() + i, name: f.name, type: "Manual", date: "2026-10-05", status: "Processing" }));
    setDocs((d) => [...added, ...d]);
  };
  const stats = [
    { label: "Total queries", value: "1,284" },
    { label: "Most common issue", value: "Low pressure" },
    { label: "Avg resolution time", value: "29 min" },
    { label: "Unresolved issues", value: "17" },
  ];
  return (
    <Shell role="admin" title="Admin dashboard" topbar={<Link href="/admin/documents" className="btn secondary">Manage documents</Link>}>
      <div className="grid4">
        {stats.map((s) => (
          <div className="card hover stat" key={s.label}><div className="muted">{s.label}</div><div className="big-num">{s.value}</div></div>
        ))}
      </div>
      <h2 className="mt">Upload documents</h2>
      <label
        className={"dropzone" + (over ? " over" : "")}
        onDragOver={(e) => { e.preventDefault(); setOver(true); }}
        onDragLeave={() => setOver(false)}
        onDrop={(e) => { e.preventDefault(); setOver(false); add(e.dataTransfer.files); }}
      >
        <input type="file" multiple hidden onChange={(e) => add(e.target.files)} />
        <strong>Drag and drop files here</strong>
        <span className="muted">or click to browse. PDF, DOCX, CSV.</span>
      </label>
      <h2 className="mt">Recently uploaded</h2>
      <div className="card list">
        {docs.map((d) => (
          <div className="list-item" key={d.id}><div><strong>{d.name}</strong><div className="muted small">{d.type} · {d.date}</div></div><StatusTag status={d.status} /></div>
        ))}
      </div>
    </Shell>
  );
}
