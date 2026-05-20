from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import time

app = Flask(__name__)
CORS(app)  # Allow all origins

# Store system boot time
boot_time = time.time()

@app.route('/')
def home():
    return "✅ DevOps Monitoring Backend is Running"

@app.route('/metrics')
def metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    uptime_seconds = int(time.time() - boot_time)

    uptime = str(uptime_seconds // 60) + " mins"

    return jsonify({
        "cpu": cpu,
        "memory": memory,
        "uptime": uptime
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)