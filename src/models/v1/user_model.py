from datetime import datetime, timedelta
import uuid

class User(object):
    
    def __init__(self) -> None:
        self.user_id : uuid = None 
        self.username : str = None
        self.password : str = None
        self.email : str = None
        self.name : str = None
        self.job_title : str = None
        self.phone_number : str = None
        self.date_registered : datetime = datetime.now()
        self.access_level : str = None
        
    
    ### functions to retrieve, update, delete users
    def login(self):
        pass
    
    def signup(self):
        pass