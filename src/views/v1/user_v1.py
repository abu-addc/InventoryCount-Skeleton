from flask import Blueprint, request, jsonify
import json

from src.utils.responses import Responses

user_v1 = Blueprint('user_v1', __name__)

@user_v1.route('/v1/user/', methods=['POST'])
### auth decorator method
def create_user():
    pass


