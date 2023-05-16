from datetime import datetime, timedelta
import uuid

from src.models.v1.user_model import User

from src.services.__init__ import MongoDBConnection
from src.utils.responses import Responses
import src.globalvars as globalvars

class Session(object):
    
    def __init__(self) -> None:
        self.session_id : uuid = None
        self.date_created : datetime = datetime.now()
        self.expiration_date : datetime = None
        self.loggedUser : User = None
        self.token : str = None
        
    
    ### functions to retrieve, delete sessions
    
    ## Create a new session when user logs in
    def create_session(self):
        pass
    
            
    