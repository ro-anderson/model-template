# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from predictor import Predictor

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api", methods=['POST'])
def predict():
    preds = request.json
    return jsonify(preds), 201


if __name__ == '__main__':
    predictor = Predictor()
    app.run(debug=True)
