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
    # def login(self):
    #     pass
    
    def signup(self, user_id, username, password, email, name, job_title, phone_number, date_registered, access_level):
        
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

            print(dataBaseConnection)
            
            # Detect user existed by email
            user_existed = dataBaseConnection.find_one({"email": email})

            if user_existed:
                return [Responses.FAIL, "This email was already used!"]


            # Create a new user document
            user_document = {
                "user_id": user_id,
                "username": username,
                "password": password,
                "email": email,
                "name": name,
                "job_title": job_title,
                "phone_number": phone_number,
                "date_registered": date_registered,
                "access_level": access_level
            }
            
            # Insert the user document into the database
            print(user_document)
            dataBaseConnection.insert_one(user_document)
            
            return [Responses.SUCCESS, self.user_id]

        except Exception as e:
            raise ValueError('Error adding new User:' f'{e}')
        
        
    


        
        
        
        
        
        
        
        
        
        
        
        
       