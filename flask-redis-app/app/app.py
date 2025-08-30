from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route("/")
def home():
    return "<h1>Welcome to the Flask + Redis App!</h1>"

@app.route("/count")
def count():
    visits = r.incr("counter")  # Increment the counter
    return jsonify(message=f"This page has been visited {visits} times.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)