from datetime import datetime
from src.models.v1.inventory_count_model import InventoryCount
from src.models.v1.event_model import Event
from src.models.v1.participant_model import Participant
from src.models.v1.user_model import User
from src.utils.libs import generate_new_inventory_uuid

from src.utils.responses import Responses

### Fetch inventory by id : Complete
def fetch_inventory(inventory_id):
    try:
        inventory = InventoryCount.find_by_inventory_id(inventory_id=inventory_id)
        
        if inventory is None:
            return [Responses.FAIL]

        return [Responses.SUCCESS, inventory] 
    except Exception as e:
        # LogHandling.exceptionHandling(error= f'{e}', origin= 'SELLOUT_CANCEL')
        raise Responses.EXCEPTION    

def fetch_itemBySku(inventory_id, sku):
    try:
        inventory = InventoryCount.find_by_inventory_id(inventory_id=inventory_id)

        if inventory is None:
            return [Responses.FAIL]
       
        item = inventory.find_item_by_sku(sku=sku)

        if item is None:
            return [Responses.FAIL]

        return [Responses.SUCCESS, item] 
    except Exception as e:
        # LogHandling.exceptionHandling(error= f'{e}', origin= 'SELLOUT_CANCEL')
        raise Responses.EXCEPTION    

def add_inventory(request_body):
    try:
        validationList = []
        
        inventoryToAdd = InventoryCount()
        
        ## validationList = InventoryCount.validate_fields(req = req)
        
        if validationList > 0:
            return [Responses.REQUIRED_FIELDS_MISSING, validationList]
        
        inventoryToAdd.inventory_id = generate_new_inventory_uuid()
        inventoryToAdd.date_created : datetime = datetime.now()
        inventoryToAdd.name = request_body.get('name', None)
        inventoryToAdd.inventory_location = request_body.get('inventory_location', None)
        inventoryToAdd.due_date = request_body('due_date', None)
        
        createdBy = User()
        createdBy.user_id = request_body.get('created_by').get('user_id', None)
        createdBy.username = request_body.get('created_by').get('username', None)
        createdBy.email = request_body.get('created_by').get('email', None)
        
        inventoryToAdd.created_by = createdBy
        inventoryToAdd.status = "Due"

        response = inventoryToAdd.add_inventory()
        return response
    except Exception as e:
        raise Responses.EXCEPTION
        

def update_inventories(inventory_id, request_body):
    try:
        inventory_to_update = InventoryCount()
        inventory_to_update.inventory_id = inventory_id

        for key, value in request_body:
            if key == 'event':
                newEvent = Event()
                newEvent.event_type = value.get('event_type', None)
                newEvent.user.email = value.get('user', None)
                newEvent.event_time = datetime.now()
                response = inventory_to_update.add_event(newEvent)
            if key == 'status':
                #inventory_to_update.update_status(value)
                pass
            if key == 'dueDate':
                #inventory_to_update.update_dueDate(value)
                pass
            if key == 'participant':
                newParticipant = Participant()
                newParticipant.user_id = value.get('user_id', None)
                newParticipant.email = value.get('email', None)
                newParticipant.username = value.get('username', None)
                inventory_to_update.add_participant(newParticipant)

        return response
    except Exception as e:
        #LogHandling.exceptionHandling(error= f'{e}', origin= 'SELLOUT_CREATION')
        raise Responses.EXCEPTION
    
def update_quantity_counted(inventory_id, request_body):
    try:
        inventory_to_update = InventoryCount()
        inventory_to_update.inventory_id = inventory_id
        sku = request_body.get('sku', None)  # Retrieve the value of the "sku" key
        print(sku)  
        quantity_counted = request_body.get('quantity_counted', None)  # Retrieve the value of the "quantity_counted" key
        user_id = request_body.get('user_id', None) # Retrieve the value of the "user_id" key
            
        if sku and quantity_counted:
            print("we here s and q")
            response = inventory_to_update.update_quatity_counted_base_on_sku(sku=sku, quantity_counted=quantity_counted)

        if user_id and quantity_counted:
            print("we here u and q")
            response = inventory_to_update.update_quatity_counted_base_on_user_id(user_id=user_id, quantity_counted=quantity_counted)

        return response
            
    except Exception as e:
        #LogHandling.exceptionHandling(error= f'{e}', origin= 'SELLOUT_CREATION')
        raise Responses.EXCEPTION
    