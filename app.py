from flask import Flask, request, jsonify
from kernel import Kernel

app = Flask(__name__)
kernel = Kernel()

@app.route("/create_process", methods=["POST"])
def create_process():
    name = request.json.get("name")
    process = kernel.create_process(name)
    return jsonify({"pid": process.pid, "name": process.name})

@app.route("/list_processes", methods=["GET"])
def list_processes():
    processes = kernel.list_processes()
    return jsonify(processes)

@app.route("/kill_process", methods=["POST"])
def kill_process():
    pid = request.json.get("pid")
    kernel.kill_process(pid)
    return jsonify({"status": "success"})

@app.route("/run_command", methods=["POST"])
def run_command():
    command = request.json.get("command")
    output = kernel.run_command(command)
    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(debug=True)
