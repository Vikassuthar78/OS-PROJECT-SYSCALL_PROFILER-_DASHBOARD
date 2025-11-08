import "./chartSetup";
import "./Dashboard.css";
import React, { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";
import Sidebar from "./components/Sidebar";

function App() {
  const [stats, setStats] = useState({});
  const [historyLabels, setHistoryLabels] = useState([]);
  const [historyCounts, setHistoryCounts] = useState([]);
  const [prevTotal, setPrevTotal] = useState(0);

  const [sidebarOpen, setSidebarOpen] = useState(true); 

  const fetchStats = async () => {
    try {
      const res = await axios.get("http://localhost:5000/stats");
      const data = res.data;

      setStats(data);

      const totalCount = Object.values(data).reduce(
        (a, b) => a + b.count,
        0
      );

      const diff = totalCount - prevTotal;
      setPrevTotal(totalCount);

      setHistoryLabels((prev) => [
        ...prev.slice(-19),
        new Date().toLocaleTimeString(),
      ]);

      setHistoryCounts((prev) => [
        ...prev.slice(-19),
        diff < 0 ? 0 : diff,
      ]);

    } catch (e) {
      console.error("Backend Error:", e);
    }
  };

  useEffect(() => {
    fetchStats();
    const interval = setInterval(fetchStats, 2000);
    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const labels = Object.keys(stats);
  const counts = labels.map((key) => stats[key].count);
  const latency = labels.map((key) => stats[key].avg_latency_ms);
  const totalEvents = counts.reduce((a, b) => a + b, 0);
  const topEvent = labels[counts.indexOf(Math.max(...counts))] || "No Data";

  return (
    <div>

      {/* ✅ SIDEBAR TOGGLE BUTTON */}
      <button
        className="toggle-btn"
        onClick={() => setSidebarOpen(!sidebarOpen)}
      >
        ☰
      </button>

      {/* ✅ SIDEBAR */}
      <Sidebar open={sidebarOpen} />

      <div className={`content ${sidebarOpen ? "shift" : ""}`}>
        <h1 className="title">Windows Syscall Profiler Dashboard</h1>

        {/* ✅ CARDS */}
        <div className="card-row">
          <div className="card">
            <h3>Total Events</h3>
            <p>{totalEvents}</p>
          </div>

          <div className="card">
            <h3>Top Event</h3>
            <p>{topEvent}</p>
          </div>

          <div className="card">
            <h3>Unique Event Types</h3>
            <p>{labels.length}</p>
          </div>
        </div>

        {/* ✅ SYSCALL FREQUENCY */}
        <div className="chart-box" id="syscall-frequency">
          <h2>Syscall Frequency</h2>
          <Bar
            data={{
              labels,
              datasets: [
                {
                  label: "Count",
                  data: counts,
                  backgroundColor: "#58a6ff",
                },
              ],
            }}
          />
        </div>

        {/* ✅ LATENCY */}
        <div className="chart-box" id="latency-chart">
          <h2>Average Latency (ms)</h2>
          <Bar
            data={{
              labels,
              datasets: [
                {
                  label: "Avg Latency (ms)",
                  data: latency,
                  backgroundColor: "#f85149",
                },
              ],
            }}
          />
        </div>

       
        {/* ✅ RAW DATA */}
        <div className="table-box" id="raw-data">
          <h2>Raw Event Data</h2>
          <table>
            <thead>
              <tr>
                <th>Event</th>
                <th>Count</th>
                <th>Avg Latency (ms)</th>
              </tr>
            </thead>
            <tbody>
              {labels.map((key) => (
                <tr key={key}>
                  <td>{key}</td>
                  <td>{stats[key].count}</td>
                  <td>{stats[key].avg_latency_ms}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

      </div>
    </div>
  );
}

export default App;
