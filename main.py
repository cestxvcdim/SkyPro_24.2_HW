import os
from flask import Flask, jsonify, request, abort
from utils import make_query_response

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route('/')
def main_page():
    greetings = {
        "message": "Hello! Input in browse string '/perform_query' and make you query",
        "params": {
            "cmd1": ["filter", "map", "unique", "sort", "limit"],
            "cmd2": ["filter", "map", "unique", "sort", "limit"],
            "value1": "Any",
            "value2": "Any",
            "filename": "<filename>.txt"
        }
    }
    return jsonify(greetings)


@app.route('/perform_query', methods=["POST"])
def query():
    data = request.json
    cmd1 = data.get("cmd1")
    cmd2 = data.get("cmd2")
    value1 = data.get("value1")
    value2 = data.get("value2")
    filename = data.get("filename")

    if not (cmd1 and value1 and filename):
        abort(400, 'You need input the minimum amount of commands (cmd1, value1, filename)!')

    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        return abort(400, 'File not found')

    with open(file_path) as file:
        result = make_query_response(cmd1, value1, file)
        if cmd2 and value2:
            result = make_query_response(cmd2, value2, result)
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
