from flask import Blueprint, request, jsonify
import json

from src.controllers.v1.user_controller import add_user
from src.utils.responses import Responses

user_v1 = Blueprint('user_v1', __name__)

@user_v1.route('/v1/user/', methods=['POST'])
### auth decorator method
def create_user():
    try:
        # req = json.loads(request.data)
        # print(req)
        request_body = request.get_json()
        print(request_body)
        response = add_user(request_body)
        
        if response[0] == Responses.FAIL:
            return jsonify({'result': Responses.FAIL.name, 'code': Responses.FAIL.value, "data": response[1]}), 400
            
        if response[0] == Responses.REQUIRED_FIELDS_MISSING:
            return jsonify({'result': Responses.REQUIRED_FIELDS_MISSING.name, 'code': Responses.REQUIRED_FIELDS_MISSING.value, "data": response[1]}), 400
        
        return jsonify({'result': Responses.SUCCESS.name,'result_code':  Responses.SUCCESS.value, "user_id": response[1]}),200    
    
    except Exception as e:
        return jsonify({'code': Responses.EXCEPTION.value}), 500
         


