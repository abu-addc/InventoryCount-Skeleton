from datetime import datetime, timedelta
import uuid

from src.models.v1.user_model import User
from src.models.v1.event_model import Event

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
    
    
        
        