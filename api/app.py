from flask import Flask, jsonify
from flask_cors import CORS
from repository import repo

app = Flask(__name__)
CORS(app, origins=['http://localhost:8080'])

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/season/<year>")
def get_season(year):
    season = repo.get_season(year)
    return jsonify(season)

app.run('127.0.0.1',8686)