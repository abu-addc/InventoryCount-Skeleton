from flask import Flask, render_template, jsonify, request
import src.globalvars as globalvars
from flask_cors import CORS

from src.views.v1.inventory_count_v1 import inventory_count_v1

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

app.register_blueprint(inventory_count_v1)

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