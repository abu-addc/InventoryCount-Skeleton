from datetime import datetime, timedelta
from src.models.v1.user_model import User

class Event(object):
    
    def __init__(self) -> None:
        self.event_type : str = None
        self.user : User = None
        self.event_time = datetime.now()
        
        
    def toJSON(self):
        return {
            "event_type": self.event_type,
            "user" : self.user,
            "event_time" : self.event_time
        }      
        
        