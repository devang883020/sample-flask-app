import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME    = os.getenv("APP_NAME", "sample-app")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENV         = os.getenv("ENV", "development")

@app.route("/")
def home():
    return jsonify({
        "app":     APP_NAME,
        "version": APP_VERSION,
        "env":     ENV,
        "message": f"Hello from {APP_NAME}! 🚀"
    })

@app.route("/health")
def health():
    # Kubernetes readiness + liveness probe hits this
    return jsonify({"status": "ok", "app": APP_NAME}), 200

@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
