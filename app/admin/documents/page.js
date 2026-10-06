"use client";
import { useState } from "react";
import Link from "next/link";
import Shell, { StatusTag } from "../../../components/Shell";
import { documents } from "../../../lib/data";

export default function Documents() {
  const [docs, setDocs] = useState(documents);
  const [type, setType] = useState("All");
  const rows = docs.filter((d) => type === "All" || d.type === type);
  const upload = (files) => {
    const added = Array.from(files).map((f, i) => ({ id: Date.now() + i, name: f.name, type: "Manual", date: "2026-10-05", status: "Processing" }));
    setDocs((d) => [...added, ...d]);
  };
  const rename = (id) => {
    const n = window.prompt("New document name:");
    if (n) setDocs((d) => d.map((x) => (x.id === id ? { ...x, name: n } : x)));
  };
  return (
    <Shell role="admin" title="Document management" topbar={
      <label className="btn primary">Bulk upload<input type="file" multiple hidden onChange={(e) => upload(e.target.files)} /></label>
    }>
      <div className="row mb">
        {["All", "Manual", "Log", "Safety"].map((t) => (
          <button key={t} className={"chip" + (type === t ? " on" : "")} onClick={() => setType(t)}>{t}</button>
        ))}
      </div>
      <div className="card tablewrap">
        <table>
          <thead><tr><th>Name</th><th>Type</th><th>Upload date</th><th>Status</th><th>Actions</th></tr></thead>
          <tbody>
            {rows.map((d) => (
              <tr key={d.id}>
                <td><strong>{d.name}</strong></td><td>{d.type}</td><td>{d.date}</td><td><StatusTag status={d.status} /></td>
                <td className="row">
                  <button className="btn ghost sm" onClick={() => window.alert("Previewing: " + d.name)}>View</button>
                  <button className="btn ghost sm" onClick={() => rename(d.id)}>Edit</button>
                  <button className="btn ghost sm danger" onClick={() => setDocs((x) => x.filter((y) => y.id !== d.id))}>Delete</button>
                </td>
              </tr>
            ))}
            {rows.length === 0 && <tr><td colSpan={5} className="muted center">No documents of this type yet.</td></tr>}
          </tbody>
        </table>
      </div>
      <p className="mt"><Link href="/admin/analytics" className="btn secondary">Go to analytics</Link></p>
    </Shell>
  );
}
