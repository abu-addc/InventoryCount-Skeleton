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
### method to verify the body of the request, so we know which function to use
def update_inventory(id):
    response = update_inventory(req = req)
    pass

### do we define different methods for the different endpoints?



