import React from "react";
import "./Sidebar.css";

export default function Sidebar({ open }) {

  const scrollToSection = (id) => {
    const s = document.getElementById(id);
    if (s) s.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <div className={`sidebar ${open ? "open" : "closed"}`}>
      <h2 className="sidebar-title">Profiler</h2>

      <ul>
        <li onClick={() => scrollToSection("syscall-frequency")}>📊 Syscall Frequency</li>
        <li onClick={() => scrollToSection("latency-chart")}>⏱ Average Latency</li>
        <li onClick={() => scrollToSection("raw-data")}>📄 Raw Data Table</li>
      </ul>
    </div>
  );
}
