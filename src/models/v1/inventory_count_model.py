from datetime import datetime, timedelta
import uuid

from src.models.v1.item_model import Item
from src.models.v1.user_model import User
from src.models.v1.event_model import Event
from src.models.v1.participant_model import Participant

from src.services.__init__ import MongoDBConnection
from src.utils.responses import Responses
import src.globalvars as globalvars

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
        self.items_counted = []
        self.status : str = None
        
    ### functions to retrieve, update, delete inventories   
    
    ## To retrieve an inventory by inventory ID
    def find_by_inventory_id(inventory_id: str):
        try:
            inventoryCount = InventoryCount()
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]
            
            inventoryFound = dataBaseConnection.find_one({"inventory_id": inventory_id})
            
            if not inventoryFound:
                return inventoryCount
            
            inventoryCount.inventory_id = inventoryFound['inventory_id']
            inventoryCount.name = inventoryFound['name']
            inventoryCount.inventory_location = inventoryFound['inventory_location']
            inventoryCount.created_by = inventoryFound['created_by']
            inventoryCount.date_created = inventoryFound['date_created']
            inventoryCount.events = inventoryFound['events']
            inventoryCount.participants = inventoryFound['participants']
            inventoryCount.items_counted = inventoryFound['items_counted']
            inventoryCount.status = inventoryFound['status']
            
            print(inventoryCount)

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
            
            itemFound = dataBaseConnection.find_one({"items_counted.sku": sku}, {"items_counted.$": 1})

            if not itemFound:
                return item
            
            item.item_name = itemFound['item_name']
            item.last_updated = itemFound['last_updated']
            item.quantity_counted = itemFound['quantity_counted']
            item.sku = itemFound['sku']

            return item
        except Exception as e:
            ##LogHandling (we need the log.py to build the authentication)
            raise Responses.EXCEPTION
        
    ## To update a quantity counted from the inventory with the specified SKU
    def update_quatity_counted_base_on_sku(self, sku, quantity_counted):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]
            
            listOfItems = []
            
            for item in self.items_counted:
                sku = item.sku
                quantity_counted = item.quantity_counted
                filter = {"inventory_id": self.inventory_id, "items_counted.sku": sku}
                update = {"$set": {"items_counted.$.quantity_counted": quantity_counted}}
                dataBaseConnection.update_one(filter, update)
        
            return Responses.SUCCESS
        except Exception as e:
            raise ValueError('Error updating quantity counted from the inventory with the specified SKU:' f'{e}')

    ## To update a quantity counted from the inventory with the specified user_id
    def update_quatity_counted_base_on_user_id(self):
        try:
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.INVENTORY_COUNT_COLLECTION]

            for participant in self.participants:
                user_id = participant['user_id']
                quantity_counted = participant['quantity_counted']
                filter = {"inventory_id": self.inventory_id, "participants.user_id": user_id}
                update = {"$set": {"participants.$.quantity_counted": quantity_counted}}
                dataBaseConnection.update_one(filter, update)
        
            return Responses.SUCCESS
        except Exception as e:
            raise ValueError('Error updating quantity counted from the inventory with the specified userID:' f'{e}')

    ## Add Participant to an inventory
    def add_participant(self, user : User):
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
                        "user_id": user.user_id,
                        "username": user.username,
                        "email": user.email
                    }
                }}
            )
        
            return Responses.SUCCESS
        except Exception as e:
            raise ValueError('Error adding participant:' f'{e}')
        
    ## Add Event to an inventory's list of events
    def add_event(self, event : Event):
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
                    "events": {
                        "event_type": event.event_type,
                        "user": event.user.email,
                        "event_time": event.event_time
                    }
                }}
            )
        
            return Responses.SUCCESS
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
                "inventory_location": self.inventory_location                 
            } 
        
            result = dataBaseConnection.insert_one(new_inventory)

            return Responses.SUCCESS
        except Exception as e:
            raise ValueError('Error adding inventory to collection:' f'{e}')
        
        