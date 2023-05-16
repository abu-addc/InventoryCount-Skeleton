from flask import Blueprint, request, jsonify
import json

from src.utils.responses import Responses

inventory_count_v1 = Blueprint('inventory_count_v1', __name__)

@inventory_count_v1.route('/v1/inventory/<id>', methods=['GET'])
### auth decorator method
def get_inventory(id):
    pass

@inventory_count_v1.route('/v1/inventory/', methods=['POST'])
### auth decorator method
def add_inventory(id):
    pass

@inventory_count_v1.route('/v1/inventory/<id>', methods=['PUT'])
### auth decorator method
### method to verify the body of the request, so we know which function to use
def update_inventory_status(id):
    pass

def update_inventory_dueDate(id):
    pass
### do we define different methods for the different endpoints?



