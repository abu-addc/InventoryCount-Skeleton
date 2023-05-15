from datetime import datetime, timedelta
import uuid

from src.models.v1.user_model import User

class Session(object):
    
    def __init__(self) -> None:
        self.session_id : uuid = None
        self.date_created : datetime = datetime.now()
        self.expiration_date : datetime = None
        self.loggedUser : User = None
        self.token : str = None