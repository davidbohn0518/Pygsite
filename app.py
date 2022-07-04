from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS
from pyscripts import pypyg


app = Flask(__name__)
CORS(app)
api = Api(app)


class Pygify(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        retStr = pypyg.pygify(data['str'])
        retJSON = {'str': retStr}
        print(retJSON)
        return jsonify(retJSON)


class Depygify(Resource):
    def post(self):
        data = request.get_json()
        retStr = pypyg.depygify(data["str"])
        retJSON = {"str": retStr}
        return jsonify(retJSON)


api.add_resource(Pygify, "/convert-to")
api.add_resource(Depygify, "/convert-from")


if __name__ == '__main__':
    app.run(debug=True)
