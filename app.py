from flask import Flask, jsonify, request
from pyscripts import pypyg


app = Flask(__name__)


@app.route("/convert-to", methods=['POST'])
def convert_to():
    data = request.get_json()
    retStr = pypyg.pygify(data["str"])
    retJSON = {"string": retStr}
    return jsonify(retJSON)


@app.route("/convert-from", methods=['POST'])
def convert_from():
    data = request.get_json()
    retStr = pypyg.depygify(data["str"])
    retJSON = {"string": retStr}
    return jsonify(retJSON)


if __name__ == '__main__':
    app.run(debug=True)
