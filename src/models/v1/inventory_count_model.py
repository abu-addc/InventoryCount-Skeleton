from datetime import datetime, timedelta
from src.models.v1.user_model import User
from src.models.v1.event_model import Event

class InventoryCount(object):
        
    def __init__(self) -> None:
        self.inventory_id: int = None
        self.name : str = None
        self.inventory_location : str = None
        self.created_by : User = None
        self.date_created : datetime = None
        self.events = []
        self.participants = []
        self.items_counted = []
        self.status : str = None
        
    ### functions to retrieve, update, delete inventories    
    
    
    
        
        