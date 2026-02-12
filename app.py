from flask import Flask, jsonify
import mysql.connector
import os
import time
from datetime import datetime

app = Flask(__name__)

# -----------------------------
# Database Connection Function
# -----------------------------
def connect_db():
    while True:
        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST", "db"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "root"),
                database=os.getenv("DB_NAME", "mydb")
            )
            print("✅ Connected to MySQL")
            return connection
        except:
            print("⏳ Waiting for MySQL...")
            time.sleep(3)

db = connect_db()

# -----------------------------
# Home Route (HTML UI)
# -----------------------------
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Two-Tier Web Architecture</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
                display: inline-block;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                color: #555;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Two-Tier Web Architecture</h1>
            <p>Flask Application running behind Nginx</p>
            <p>Connected to MySQL Database</p>
            <p><strong>Status:</strong> Running Successfully</p>
        </div>
    </body>
    </html>
    """

# -----------------------------
# Health Check Route (JSON)
# -----------------------------
@app.route("/health")
def health():
    return jsonify({
        "application": {
            "name": "Two-Tier Web Architecture",
            "version": "1.0.0",
            "environment": "production"
        },
        "architecture": {
            "backend": "Flask (Python)",
            "database": "MySQL",
            "web_server": "Nginx",
            "containerization": "Docker"
        },
        "status": "Running Successfully",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
