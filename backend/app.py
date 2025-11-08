from flask import Flask, jsonify
from flask_cors import CORS
from syscall_trace import SyscallProfiler

app = Flask(__name__)
CORS(app)

profiler = SyscallProfiler()
profiler.start()


@app.route("/stats", methods=["GET"])
def stats():
    output = {}

    for name, value in profiler.stats.items():

        events = value.get("events", [])
        count = value.get("count", 0)
        total = value.get("total", 0)

        avg = (total / count) if count > 0 else 0

        output[name] = {
            "count": count,
            "avg_latency_ms": round(avg, 3),  
            "events": events[-20:]
        }

    return jsonify(output)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Syscall monitoring running"})


if __name__ == "__main__":
    print("✅ Backend running on http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
