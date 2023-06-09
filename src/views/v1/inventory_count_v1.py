from flask import Blueprint, request, jsonify
import json

from src.controllers.v1.inventory_count_controller import update_inventories, add_inventory, update_quantity_counted, fetch_inventory, fetch_itemBySku, get_inventories_by_user
from src.utils.responses import Responses

inventory_count_v1 = Blueprint('inventory_count_v1', __name__)

### Returns one inventory based on the inventory's id : Completed
@inventory_count_v1.route('/v1/inventory/<inventory_id>', methods=['GET'])
### auth decorator method
def get_inventory(inventory_id):
    try:
        inventory_id = {"inventory_id": inventory_id}
        response = fetch_inventory(inventory_id=inventory_id)
        print(response)
        
        if response[0] == Responses.FAIL:
            return jsonify({'result': Responses.FAIL.name, 'code': Responses.FAIL.value, "data": response[1]}), 400
        
        return jsonify({'result': Responses.SUCCESS.name,'result_code':  Responses.SUCCESS.value, 'data': response[1].toJSON() }),200
    except Exception as e:
        return jsonify({'code': Responses.EXCEPTION.value}), 500

### Returns the item based on SKU: Completed
@inventory_count_v1.route('/v1/inventory/<inventory_id>/getItem/<sku>', methods=['GET'])
### auth decorator method
def get_item(inventory_id, sku):
    try:
        inventory_id = {"inventory_id": inventory_id}
        inventory = fetch_inventory(inventory_id)
        print(inventory)

        if inventory[0] == Responses.FAIL:
            return jsonify({'result': Responses.FAIL.name, 'code': Responses.FAIL.value, "data": inventory[1]}), 400

        items = inventory[1].items_counted
        print(items)

        for item in items:
            if item['sku'] == sku:
                return jsonify(item), 200
            # If the item with the provided SKU is not found
            
        return jsonify({'result': 'Item not found.'}), 404
    
    
    except Exception as e:
        return jsonify({'code': Responses.EXCEPTION.value}), 500

### add a new inventory
@inventory_count_v1.route('/v1/inventory/', methods=['POST'])
### auth decorator method

def post_inventory():
       
    request_body = request.get_json()
    
    response = add_inventory(request_body)
    print (request_body)
    print (response)
    
    try: 
        
        if response[0] == Responses.FAIL:
            return jsonify({'result': Responses.FAIL.name, 'code': Responses.FAIL.value, "data": response[1]}), 400

        if response[0] == Responses.REQUIRED_FIELDS_MISSING:
            return jsonify({'result': Responses.REQUIRED_FIELDS_MISSING.name, 'code': Responses.REQUIRED_FIELDS_MISSING.value, "data": response[1]}), 400

        return jsonify({'result': Responses.SUCCESS.name, 'result_code': Responses.SUCCESS.value, "data": response[1]}), 200

    except Exception as e:
        return jsonify({'code': Responses.EXCEPTION.value}), 500
    
### update an existing inventory's status, dueDate
### add an event or participant to the inventory    
@inventory_count_v1.route('/v1/inventory/<inventory_id>/update/<key>', methods=['PUT'])
### auth decorator method
def update_inventory_view(inventory_id, key):
    try:
        print("view")
        #req = json.loads(request.data)
        request_body = request.get_json()
        print(request_body)
        response = update_inventories(inventory_id, key, request_body)
        print(response)
        
        if response[0] == Responses.FAIL:
            return jsonify({'result': Responses.FAIL.name, 'code': Responses.FAIL.value, "data": response[1]}), 400
            
        if response[0] == Responses.REQUIRED_FIELDS_MISSING:
            return jsonify({'result': Responses.REQUIRED_FIELDS_MISSING.name, 'code': Responses.REQUIRED_FIELDS_MISSING.value, "data": response[1]}), 400
        
        return jsonify({'result': Responses.SUCCESS.name,'result_code': Responses.SUCCESS.value, "inventory_id": response[1] }), 200
    except Exception as e:
        return jsonify({'code': Responses.EXCEPTION.value}), 500
        
### update inventory_quantity_counted: Completed
@inventory_count_v1.route('/v1/inventoryCount/<inventory_id>', methods=['PUT'])
### auth decorator method
def update_quantity_counted_view(inventory_id):
    try:
        #req = json.loads(request.data)
        # inventory_id = {"inventory_id": inventory_id}
        request_body = request.get_json()

        print(request_body)
            
        response = update_quantity_counted(inventory_id, request_body)
            
        if response[0] == Responses.FAIL:
            return jsonify({'result': Responses.FAIL.name, 'code': Responses.FAIL.value, "data": response[1]}), 400
                
        if response[0] == Responses.REQUIRED_FIELDS_MISSING:
            return jsonify({'result': Responses.REQUIRED_FIELDS_MISSING.name, 'code': Responses.REQUIRED_FIELDS_MISSING.value, "data": response[1]}), 400
            
        return jsonify({'result': Responses.SUCCESS.name,'result_code':  Responses.SUCCESS.value, 'inventory_id': response[1] }), 200
    
    except Exception as e:
        return jsonify({'code': Responses.EXCEPTION.value}), 500


### Returns user's list of inventories
@inventory_count_v1.route('/v1/inventories/<user_id>', methods=['GET'])
### auth decorator method
def get_inventories(user_id):
    try:
        ##user_id = {"user_id": user_id} 
        response = get_inventories_by_user(user_id)
        inventories = list()
        for inventory in response[1]:
            inventories.append(inventory.toJSON())
        if response[0] == Responses.FAIL:
            return jsonify({'result': Responses.FAIL.name, 'code': Responses.FAIL.value, "data": response[1]}), 400

        return jsonify({'result': Responses.SUCCESS.name,'result_code':  Responses.SUCCESS.value, 'data': inventories }),200
    except Exception as e:
        return jsonify({'code': Responses.EXCEPTION.value}), 500

