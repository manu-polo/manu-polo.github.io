
from flask import Flask, render_template, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run-python", methods=["POST"])
def run_python():
    result = subprocess.run(
        [sys.executable, "file_io.py"],
        capture_output=True,
        text=True
    )

    return jsonify({
        "output": result.stdout if result.returncode == 0 else result.stderr
    })

