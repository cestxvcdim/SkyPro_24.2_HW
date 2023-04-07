import os
from flask import Flask, jsonify, request, abort, Response
from typing import Union, Optional, List, Any
from dataclasses import asdict
from utils import make_query_response, get_greetings, Greetings
from greet import greetings as g

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route('/')
def main_page() -> Response:
    greetings: Greetings = get_greetings(g)
    return jsonify(asdict(greetings))


@app.route('/perform_query', methods=["POST"])
def query() -> Response:
    data: Optional[Any] = request.json
    if not data:
        return jsonify({"message": "Data is empty"})
    cmd1: Optional[str] = data.get("cmd1")
    cmd2: Optional[str] = data.get("cmd2")
    value1: Optional[str] = data.get("value1")
    value2: Optional[str] = data.get("value2")
    filename: Optional[str] = data.get("filename")

    if not (cmd1 and value1 and filename):
        abort(400, 'You need input the minimum amount of commands (cmd1, value1, filename)')

    file_path: str = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        abort(400, 'File not found')

    with open(file_path) as file:
        result: Union[str, List] = make_query_response(cmd1, value1, file)
        if cmd2 and value2:
            result2: Union[str, List] = make_query_response(cmd2, value2, result)
            return jsonify(result2)
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
