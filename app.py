from flask import Flask, request, jsonify
from model import get_solution
from db import cursor, conn
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Sentinel-AIOps API is running"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    log = data.get("log")

    if not log:
        return jsonify({"error": "No log provided"}), 400

    solution = get_solution(log)

    # Store in DB
    cursor.execute(
        "INSERT INTO logs (log, solution) VALUES (%s, %s)",
        (log, solution)
    )
    conn.commit()

    return jsonify({
        "log": log,
        "solution": solution,
        "timestamp": str(datetime.datetime.now())
    })

# ✅ IMPORTANT FIX FOR RENDER
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)