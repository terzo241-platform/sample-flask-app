from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "0.1.0"


@app.route("/")
def home():
    return jsonify({"message": "Hello from sample-flask-app", "status": "ok", "version": VERSION})


@app.route("/version")
def version():
    return jsonify({"version": VERSION})


@app.route("/health")
def health():
    return jsonify({"healthy": True})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
