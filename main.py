from flask import Flask, jsonify, request
from scripts import pypyg
g

app = Flask(__name__)


@app.route("/convert-to", methods=['GET'])
def convert_to():
    return '<p>convert to Test<p>'


@app.route("/convert-from", methods=['GET'])
def convert_from():
    return '<p>convert from Test<p>'


if __name__ == '__main__':
    app.run(debug=True)

string = "hello"

pypyg.pygify(string)
