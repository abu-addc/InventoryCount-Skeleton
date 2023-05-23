from datetime import datetime

from src.models.v1.user_model import User
from src.utils.libs import generate_new_user_uuid

from src.utils.responses import Responses


## Abu: Using body request, we can set the properties of the user
def add_user(req):
    try:
        # validationList = []
        
        userToAdd = User()
        
        ## validationList = InventoryCount.validate_fields(req = req)
        
        # if validationList > 0:
        #     return [Responses.REQUIRED_FIELDS_MISSING, validationList]
        
        userToAdd.user_id = generate_new_user_uuid()
        userToAdd.username = req.get("username")
        userToAdd.password = req.get("password")
        userToAdd.email = req.get("email")
        userToAdd.name = req.get("name")
        userToAdd.job_title = req.get("job_title")
        userToAdd.phone_number = req.get("phone_number")
        userToAdd.date_registered: datetime = datetime.now()
        userToAdd.access_level = "Regular user"

        userToAdd.user_id

        response = userToAdd.signup()
        return response
    except Exception as e:
        raise Responses.EXCEPTION
    
    
def sign_in(request_body):
    try: 
        
        pass
    except Exception as e:
        raise Responses.EXCEPTION    


