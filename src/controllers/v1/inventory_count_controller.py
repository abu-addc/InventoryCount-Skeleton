from datetime import datetime
from src.models.v1.inventory_count_model import InventoryCount
from src.utils.libs import generate_new_inventory_uuid

from src.utils.responses import Responses


def fetch_inventory(inventory_id):
    print("controller")
    try:
        inventory = InventoryCount.find_by_inventory_id(inventory_id= inventory_id)
        if inventory is None:
            return [Responses.FAIL]
        
        print(inventory.inventory_id )

        return [Responses.SUCCESS, inventory] 
    except Exception as e:
        # LogHandling.exceptionHandling(error= f'{e}', origin= 'SELLOUT_CANCEL')
        raise Responses.EXCEPTION    

def fetch_itemBySku(sku):
    try:
        item = InventoryCount.find_item_by_sku(sku=sku)
        if item is None:
            return [Responses.FAIL]

        print(item.sku)
        
        return [Responses.SUCCESS, item] 
    except Exception as e:
        # LogHandling.exceptionHandling(error= f'{e}', origin= 'SELLOUT_CANCEL')
        raise Responses.EXCEPTION    

def add_inventory(req):
    try:
        validationList = []
        
        inventoryToAdd = InventoryCount()
        
        ## validationList = InventoryCount.validate_fields(req = req)
        
        if validationList > 0:
            return [Responses.REQUIRED_FIELDS_MISSING, validationList]
        
        inventoryToAdd.inventory_id = generate_new_inventory_uuid()
        inventoryToAdd.createdAt: datetime = datetime.now()
        inventoryToAdd.name = req.get('name', None)
        inventoryToAdd.inventory_location = req.get('inventory_location', None)
        ## what else is sent in the request?

        inventoryToAdd.add_inventory()
        return [Responses.SUCCESS] 
    except Exception as e:
        raise Responses.EXCEPTION
        

def update_inventories(id, request_body):
    try:
        inventory_to_update = InventoryCount()
        #inventory_to_update = inventory_to_update.find_by_inventory_id(id)
        for key, value in request_body:
            if key == 'events':
                inventory_to_update.add_event(value)
            if key == 'status':
                #inventory_to_update.update_status(value)
                pass
            if key == 'dueDate':
                #inventory_to_update.update_dueDate(value)
                pass
            if key == 'participants':
                inventory_to_update.add_participant(value)

    except Exception as e:
        #LogHandling.exceptionHandling(error= f'{e}', origin= 'SELLOUT_CREATION')
        raise Responses.EXCEPTION
    ### loop through the key, values of the request's body
    ### verify the key, then call the appropriate method from the model
    
def update_quantity_counted(inventory_id, request_body):
    try:
        inventory_to_update = InventoryCount()
        sku = request_body.get('sku')  # Retrieve the value of the "sku" key
        quantity_counted = request_body.get('quantity_counted')  # Retrieve the value of the "quantity_counted" key
        user_id = request_body.get('user_id') # Retrieve the value of the "user_id" key
            
        if sku and quantity_counted:
            inventory_to_update.update_quatity_counted_base_on_sku(sku=sku, quantity_counted=quantity_counted)

        if user_id and quantity_counted:
            inventory_to_update.update_quatity_counted_base_on_user_id(user_id=user_id, quantity_counted=quantity_counted)
            
    except Exception as e:
        #LogHandling.exceptionHandling(error= f'{e}', origin= 'SELLOUT_CREATION')
        raise Responses.EXCEPTION
    