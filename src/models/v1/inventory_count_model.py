from datetime import datetime, timedelta
import uuid
import json

from src.models.v1.item_model import Item
from src.models.v1.user_model import User
from src.models.v1.event_model import Event
from src.models.v1.participant_model import Participant

from src.utils.custom_encoder import CustomEncoder

from src.services.__init__ import MongoDBConnection
from src.utils.responses import Responses
import src.globalvars as globalvars

from pymongo import MongoClient

class InventoryCount(object):
        
    def __init__(self) -> None:
        self.inventory_id: uuid = None
        self.name : str = None
        self.inventory_location : str = None
        self.created_by : User = None
        self.date_created : datetime = None
        self.due_date : datetime = None
        self.events = []
        self.participants = []
        self.items_counted : Item = None
        self.status : str = None
          
    def toJSON(self):
        return {
            "inventory_id": self.inventory_id,
            "name" : self.name,
            "inventory_location" : self.inventory_location,
            "created_by" : self.created_by,
            "date_created": self.date_created,
            "due_date": self.due_date,
            "events": self.events,
            "participants": self.participants,
            "items_counted": self.items_counted,
            "status": self.status
        }  
    
    def toJSONList(self):
        JSONList = list()
        for item in self:
            JSONList.append(self.toJSON(item))
        return JSONList
    
    ### functions to retrieve, update, delete inventories 
    ## To retrieve an inventory by inventory ID
    def find_by_inventory_id(inventory_id: str):
        try:
            inventoryCount = InventoryCount()
            dataBaseConnection = MongoDBConnection.dataBase(
            )[globalvars.INVENTORY_COUNT_COLLECTION]
            
            inventoryFound = dataBaseConnection.find_one(inventory_id)
            
            if not inventoryFound:
                return inventoryCount

            inventoryCount.inventory_id = inventoryFound['inventory_id']
            inventoryCount.name = inventoryFound['name']
            inventoryCount.inventory_location = inventoryFound['inventory_location']
            inventoryCount.created_by = inventoryFound['created_by']
            inventoryCount.date_created = inventoryFound['date_created']
            ##
            inventoryCount.due_date = inventoryFound['due_date']
            ##
            inventoryCount.events = inventoryFound['events']
            inventoryCount.participants = inventoryFound['participants']
            inventoryCount.items_counted = inventoryFound['items_counted']
            inventoryCount.status = inventoryFound['status']
            
            return inventoryCount
        except Exception as e:
            ##LogHandling (we need the log.py to build the authentication)
            raise Responses.EXCEPTION

    ## To retrive an item from the inventory by SKU
    def find_item_by_sku(sku: str):
        try:
            item = Item()
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]
            
            print(sku)
            itemFound = dataBaseConnection.find_one({"items_counted.sku": sku}, {"items_counted.$": 1})

            
            print(itemFound)

            if not itemFound:
                return item
            
            item.sku = itemFound['sku']
            item.item_name = itemFound['item_name']
            item.last_updated = itemFound['last_updated']
            item.quantity_counted = itemFound['quantity_counted']

            print(item.item_name)
            print(item.quantity_counted)

            return item
        except Exception as e:
            ##LogHandling (we need the log.py to build the authentication)
            raise Responses.EXCEPTION
        
    ## To update a quantity counted from the inventory with the specified SKU
    def update_quatity_counted_base_on_sku(self, sku, quantity_counted):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

            print(self.inventory_id)
 
            # filter = {"inventory_id": self.inventory_id, "items_counted.sku": sku}
            # update = {"$set": {"items_counted.$.quantity_counted": quantity_counted}}
            # dataBaseConnection.update_one(filter, update)
            dataBaseConnection.update_one(
            {"inventory_id": self.inventory_id, "items_counted.sku": sku}, 
            {"$set": {"items_counted.$.quantity_counted": quantity_counted}}
            )

            return [Responses.SUCCESS, self.inventory_id]
        except Exception as e:
            raise ValueError('Error updating quantity counted from the inventory with the specified SKU:' f'{e}')

    ## To update a quantity counted from the inventory with the specified user_id
    def update_quatity_counted_base_on_user_id(self, user_id, quantity_counted):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

           
            filter = {"inventory_id": self.inventory_id, "participants.user_id": user_id}
            update = {"$set": {"participants.$.quantity_counted": quantity_counted}}
            dataBaseConnection.update_one(filter, update)
        
            return [Responses.SUCCESS, self.inventory_id]
        except Exception as e:
            raise ValueError('Error updating quantity counted from the inventory with the specified userID:' f'{e}')

    ## Adds participant to an Inventory
    def add_participant(self, user_id, username, email):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

            inventoryCount = InventoryCount()
            inventoryFound = dataBaseConnection.find_one({"inventory_id": self.inventory_id})

            if not inventoryFound:
                return inventoryCount
            
            result = dataBaseConnection.update_one(
                {"inventory_id": self.inventory_id},
                {"$push": {
                    "participants": {
                        "user_id": user_id,
                        "username": username,
                        "email": email
                    }
                }}
            )

            print(result)
        
            return [Responses.SUCCESS, self.inventory_id]
        except Exception as e:
            raise ValueError('Error adding participant:' f'{e}')
        
    ## Adds Event to an inventory's list of events
    def add_event(self, event_type, email, event_time):
        try:
            print("model")
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

            inventoryCount = InventoryCount()
            inventoryFound = dataBaseConnection.find_one({"inventory_id": self.inventory_id})
            print(inventoryFound)

            if not inventoryFound:
                return inventoryCount
            
            result = dataBaseConnection.update_one(
                {"inventory_id": self.inventory_id},
                {"$push": {
                    "events": {
                        "event_type": event_type,
                        "user": email,
                        "event_time": event_time
                    }
                }}
            )

            print(result)
        
            return [Responses.SUCCESS, self.inventory_id]
        except Exception as e:
            raise ValueError('Error adding event to list of events:' f'{e}')
        
    ## Adds item to an inventory's list of items
    def add_item(self, item : Item):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

            inventoryCount = InventoryCount()
            inventoryFound = dataBaseConnection.find_one({"inventory_id": self.inventory_id})

            if not inventoryFound:
                return inventoryCount
            
            result = dataBaseConnection.update_one(
                {"inventory_id": self.inventory_id},
                {"$push": {
                    "items_counted": {
                        "sku": item.sku,
                        "item_name": item.item_name,
                        "location" : item.location,
                        "quantity_counted": item.quantity_counted,
                        "last_updated" : item.last_updated
                    }
                }}
            )
        
            return [Responses.SUCCESS, item.sku]
        except Exception as e:
            raise ValueError('Error adding event to list of events:' f'{e}')    
        
    ## Add new inventory to collection
    def add_inventory(self):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]
            
            new_inventory = { 
                "inventory_id": self.inventory_id,
                "name": self.name,
                "created_by" : self.created_by,
                "inventory_location": self.inventory_location,
                "events": {},
                "participants": {},
                "items_counted": {},
                "due_date": self.due_date,
                "date_created": self.date_created,
                "status": self.status       
            }
            result = dataBaseConnection.insert_one(new_inventory)
            print(result)

            return [Responses.SUCCESS, self.inventory_id]
        except Exception as e:
            raise ValueError('Error adding inventory to collection:' f'{e}')
        
        
    ## To update inventory status with the specified inventory_id
    def update_status(self, status):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

            # Update the status field of the inventory document
            dataBaseConnection.update_one(
                {"inventory_id": self.inventory_id},
                {"$set": {"status": status}})

            return [Responses.SUCCESS, self.inventory_id]
        except Exception as e:
            raise ValueError('Error updating the status on the inventory:' f'{e}')

    ## To update inventory due_date with the specified inventory_id
    def update_dueDate(self, due_date):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

            ##
            ##To convert to formatted date (same format in DB)
            ## if the user put "11-05-2023", it is going to be "Thu, 11 May 2023 00:00:00 GMT"
            date_obj = datetime.strptime(due_date, "%d-%m-%Y")
            formatted_date = date_obj.strftime("%a, %d %b %Y %H:%M:%S GMT")
            ##


            # Update the status field of the inventory document
            result = dataBaseConnection.update_one(
                {"inventory_id": self.inventory_id},
                {"$set": {"due_date": formatted_date}})
            ## ## ## ## ## ## ## ## ## I changed ^ too.

            return [Responses.SUCCESS, self.inventory_id]
        except Exception as e:
            raise ValueError('Error updating the due date of the inventory:' f'{e}')
    
     ## To retreive a list of inventories by user id
    def get_all_inventories_by_user_id(user_id):
        try:

            inventoryCount = InventoryCount()
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

            inventoriesFound = list(dataBaseConnection.find({"created_by.user_id": user_id}))
            if not inventoriesFound:
                return inventoryCount
            # Serialize inventories to JSON with the custom encoder
            # inventoriesFound = json.dumps(inventoriesFound, cls=CustomEncoder)
            inventories = list()
            for x in inventoriesFound:
                inventory = InventoryCount()
                inventory.inventory_id = x['inventory_id']
                inventory.name = x['name']
                inventory.inventory_location = x['inventory_location']
                inventory.created_by = x['created_by']
                inventory.date_created = x['date_created']
                inventory.events = x['events']
                inventory.participants = x['participants']
                inventory.items_counted = x['items_counted']
                inventory.status = x['status']
                inventories.append(inventory) 
                 
            return inventories
        except Exception as e:
            ##LogHandling (we need the log.py to build the authentication)
            raise Responses.EXCEPTION
