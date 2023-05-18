from datetime import datetime, timedelta
import uuid

from src.services.__init__ import MongoDBConnection
from src.utils.responses import Responses
import src.globalvars as globalvars

from pymongo import MongoClient

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
        
        '''
        in the body of the request we need this information:  
        "users": {
                        "username": user.username,
                        "password": user.password,
                        "email": user.email,
                        "name": user.name,
                        "job_title": user.job_title,
                        "phone_number": user.phone_number
                    }
       
        '''
        try:
            
            dataBaseConnection = MongoDBConnection.dataBase(                
            )[globalvars.USER_COLLECTION]
            
            
            # Check if the email already exists in the database (--we should ask Product Team--)
            existing_user = dataBaseConnection.find_one({"email": self.email})
            if existing_user:
                return ValueError("Username already exists.")

            # Create a new user document
            user_document = {
                "username": self.username,
                "password": self.password,
                "email": self.email,
                "name": self.name,
                "job_title": self.job_title,
                "phone_number": self.phone_number,
                }
            
            # Insert the user document into the database
            result = dataBaseConnection.insert_one(user_document)

            if result:
                return Responses.SUCCESS
            else:
                return Responses.FAIL

        except Exception as e:
            raise ValueError('Error adding new User:' f'{e}')
        
        
        # def user_exists(email : str):
        #     ### verify if the email already exists
        
        
        
        
        
        
        
        
        
        
        
        
       