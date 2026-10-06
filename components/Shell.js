"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const techNav = [
  { label: "Home", href: "/dashboard", icon: "⌂" },
  { label: "Ask AI", href: "/chat", icon: "✦" },
  { label: "Machine History", href: "/history", icon: "☰" },
  { label: "Profile", href: "/dashboard", icon: "☺", key: "profile" },
  { label: "Logout", href: "/login", icon: "⎋" },
];
const adminNav = [
  { label: "Dashboard", href: "/admin", icon: "⌂" },
  { label: "Documents", href: "/admin/documents", icon: "▤" },
  { label: "Analytics", href: "/admin/analytics", icon: "▥" },
  { label: "Logout", href: "/login", icon: "⎋" },
];

export default function Shell({ role = "tech", title, topbar, children }) {
  const path = usePathname();
  const nav = role === "admin" ? adminNav : techNav;
  const isActive = (n) => !n.key && n.label !== "Logout" && (path === n.href || (n.href !== "/admin" && path.startsWith(n.href) && n.href !== "/dashboard") || (n.href === "/dashboard" && (path === "/dashboard" || path === "/answer")));
  return (
    <div className="shell">
      <aside className="sidebar">
        <div className="brand"><span className="logo">F</span> FixIt Assistant</div>
        <nav>
          {nav.map((n) => (
            <Link key={n.label} href={n.href} className={"navlink" + (isActive(n) ? " active" : "")}>
              <span className="navicon">{n.icon}</span>{n.label}
            </Link>
          ))}
        </nav>
        <div className="sidefoot">{role === "admin" ? "Admin · A. Rahman" : "Technician · S. Kumar"}</div>
      </aside>
      <div className="main">
        <header className="topbar">
          <h1>{title}</h1>
          <div className="topright">{topbar}</div>
        </header>
        <main className="content">{children}</main>
      </div>
    </div>
  );
}

export function StatusTag({ status }) {
  const map = { Resolved: "green", Processed: "green", Running: "green", Pending: "amber", Processing: "amber", Maintenance: "amber", Escalated: "red", Failed: "red", Fault: "red" };
  return <span className={"tag " + (map[status] || "gray")}>{status}</span>;
}
