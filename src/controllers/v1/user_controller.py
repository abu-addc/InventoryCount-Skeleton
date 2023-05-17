from datetime import datetime

from src.models.v1.user_model import User
from src.utils.libs import generate_new_user_uuid

from src.utils.responses import Responses

def add_user(req):
    try:
        validationList = []
        
        userToAdd = User()
        
        userToAdd.username = req.get["username", None]
        userToAdd.password = req.get["password", None]
        userToAdd.email = req.get["email", None]
        userToAdd.name = req.get["name", None]
        userToAdd.job_title = req.get["job_title", None]
        userToAdd.phone_number = req.get["phone_number", None]
        
        
        ## validationList = InventoryCount.validate_fields(req = req)
        
        if validationList > 0:
            return [Responses.REQUIRED_FIELDS_MISSING, validationList]
        
        
        
        
        userToAdd.user_id = generate_new_user_uuid()
        userToAdd.date_registered: datetime = datetime.now()
        
        # For initialize this value we use 'Regular user' (we need to validate with Product Team) we don't know if we need this field
        userToAdd.access_level = 'Regular User'

        userToAdd.signup()
        return [Responses.SUCESS] 
    except Exception as e:
        raise Responses.EXCEPTION




