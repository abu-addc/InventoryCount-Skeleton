from flask import Flask, render_template, jsonify
import src.globalvars as globalvars
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

## app.register_blueprint(stores_v1)

CORS(app, supports_credentials= True)

@app.route("/")
def index():
    return globalvars.CONST_MONGO_URL


@app.errorhandler(404)
def errorHandle_404(self):
    return "error 404"

@app.errorhandler(500)
def errorHandle_500(self):
    return "error 500"


if __name__ == "__main__":
    app.run()