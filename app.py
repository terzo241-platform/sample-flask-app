import subprocess

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Hello from sample-flask-app", "status": "ok"})


@app.route("/health")
def health():
    return jsonify({"healthy": True})


# === DELIBERATELY VULNERABLE ENDPOINTS (Day 3 Security Scan Test) ===
# These exist ONLY to validate that security scanning catches real issues.
# Remove after verifying scans work.

@app.route("/unsafe/exec")
def unsafe_exec():
    """Bandit B102 + CodeQL: command injection via user input"""
    cmd = request.args.get("cmd", "echo hello")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return jsonify({"output": result.stdout})


@app.route("/unsafe/eval")
def unsafe_eval():
    """Bandit B307 + CodeQL: eval of user-supplied expression"""
    expr = request.args.get("expr", "1+1")
    return jsonify({"result": str(eval(expr))})


@app.route("/unsafe/sql")
def unsafe_sql():
    """Bandit B608 + CodeQL: SQL injection via string formatting"""
    user_id = request.args.get("id", "1")
    query = "SELECT * FROM users WHERE id = " + user_id
    return jsonify({"query": query})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
