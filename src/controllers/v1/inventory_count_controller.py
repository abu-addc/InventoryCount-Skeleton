from datetime import datetime

from src.models.v1.inventory_count_model import InventoryCount
from src.utils.libs import generate_new_inventory_uuid

from src.utils.responses import Responses


def add_inventory(req):
    try: 
        validationList = []
        
        inventoryToAdd = InventoryCount()
        
        ## validationList = InventoryCount.validate_fields(req = req)
        
        if validationList > 0:
            return [Responses.REQUIRED_FIELDS_MISSING, validationList]
        
        inventoryToAdd.inventory_id = generate_new_inventory_uuid()
        inventoryToAdd.createdAt: datetime = datetime.now()

        inventoryToAdd.add()
        return [Responses.SUCESS] 
    except Exception as e:
        raise Responses.EXCEPTION
        

def update_inventory(req, id):
    pass