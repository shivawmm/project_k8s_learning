from flask import Flask
import os
import os

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("ENV", "UNKNOWN")
    return f"Hello from Shivam's DevOps Project 🚀 - this is from {env} environment. image updator will work now"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)