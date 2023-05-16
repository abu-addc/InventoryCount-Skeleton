from flask import Blueprint, request, jsonify
import json

from controllers.v1.inventory_count_controller import update_inventory, add_inventory
from src.utils.responses import Responses

inventory_count_v1 = Blueprint('inventory_count_v1', __name__)

@inventory_count_v1.route('/v1/inventory/<id>', methods=['GET'])
### auth decorator method
def get_inventory(id):
    pass

@inventory_count_v1.route('/v1/inventory/', methods=['POST'])
### auth decorator method
def add_inventory(id):
    response = add_inventory()
    pass

@inventory_count_v1.route('/v1/inventory/<id>', methods=['PUT'])
### auth decorator method
def update_inventory(id):
    try:
        #req = json.loads(request.data)
        inventoryId = request.args.to_dict()
        request_body = request.get_json()
        
        response = update_inventory(inventoryId, request_body)
        
        if response[0] == Responses.FAIL:
            return jsonify({'result': Responses.FAIL.name, 'code': Responses.FAIL.value, "data": response[1]}), 400
            
        if response[0] == Responses.REQUIRED_FIELDS_MISSING:
            return jsonify({'result': Responses.REQUIRED_FIELDS_MISSING.name, 'code': Responses.REQUIRED_FIELDS_MISSING.value, "data": response[1]}), 400
        
        return jsonify({'result': Responses.SUCESS.name,'result_code':  Responses.SUCESS.value, 'sellout_id': response[1], 'total_points': response[2]}),200
    
    except Exception as e:
        return jsonify({'code': Responses.EXCEPTION.value}), 500
        
    




