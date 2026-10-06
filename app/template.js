"use client";
// template.js remounts on every navigation, so the CSS animation replays: 300ms ease-in-out slide/fade.
export default function Template({ children }) {
  return <div className="page-transition">{children}</div>;
}
