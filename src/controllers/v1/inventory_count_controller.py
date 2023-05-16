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

        inventoryToAdd.add_inventory()
        return [Responses.SUCESS] 
    except Exception as e:
        raise Responses.EXCEPTION
        

def update_inventories(id, request_body):
    try:
        inventory_to_update = InventoryCount()
        #inventory_to_update = inventory_to_update.find_by_inventory_id(id)
        for key, value in request_body:
            if key == 'event':
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
    
    # for key, value in request:
        
    #     if key == "status":
    #         inventory.updateStatus()
            
    #     if key == "dueDate":
    #         inventory.update_dueDate()   
            
    #     if key == "participant":
                 
    
    # {
    #     "status": "Done",
    #     "dueDate": "March 5th, 2023",
    #     "event": Event()
    # }
    pass
