"use client";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Login() {
  const router = useRouter();
  const [role, setRole] = useState("tech");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const submit = (e) => {
    e.preventDefault();
    if (!email.includes("@") || password.length < 4) {
      setError("Enter a valid email and a password of at least 4 characters.");
      return;
    }
    router.push(role === "admin" ? "/admin" : "/dashboard");
  };

  return (
    <div className="login-wrap">
      <div className="login-card card">
        <div className="login-logo"><span className="logo big">F</span></div>
        <h1 className="center">FixIt Assistant</h1>
        <p className="muted center">Sign in to get source-referenced fixes.</p>
        <div className="toggle" role="tablist">
          <button type="button" className={role === "tech" ? "on" : ""} onClick={() => setRole("tech")}>Technician</button>
          <button type="button" className={role === "admin" ? "on" : ""} onClick={() => setRole("admin")}>Admin</button>
        </div>
        <form onSubmit={submit}>
          <label className="field">Email
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="name@factory.com" />
          </label>
          <label className="field">Password
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Your password" />
          </label>
          {error && <p className="err">{error}</p>}
          <button type="submit" className="btn primary block">Log in as {role === "admin" ? "Admin" : "Technician"}</button>
        </form>
        <p className="center small"><a href="#" onClick={(e) => e.preventDefault()}>Forgot password?</a></p>
      </div>
    </div>
  );
}
