from flask import Flask, render_template, jsonify
import src.globalvars as globalvars
from flask_cors import CORS

from pymongo import MongoClient
from dotenv.main import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ['CONST_MONGO_URL']

client = MongoClient(MONGO_URI)

print(MONGO_URI)
print("it reached here")

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

## app.register_blueprint(stores_v1)

CORS(app, supports_credentials= True)

@app.route("/")
def index():
    return MONGO_URI


@app.errorhandler(404)
def errorHandle_404(self):
    return "error 404"

@app.errorhandler(500)
def errorHandle_500(self):
    return "error 500"


if __name__ == "__main__":
    app.run()