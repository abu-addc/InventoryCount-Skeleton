from datetime import datetime

from src.models.v1.user_model import User
from src.utils.libs import generate_new_user_uuid

from src.utils.responses import Responses


## Abu: Using body request, we can set the properties of the user
def add_user(request_body):
    try:
        # validationList = []
        
        userToAdd = User()
        
        ## validationList = InventoryCount.validate_fields(req = req)
        
        # if validationList > 0:
        #     return [Responses.REQUIRED_FIELDS_MISSING, validationList]
        
        user_id = generate_new_user_uuid()
        username = request_body.get('username')
        password = request_body.get('password')
        email = request_body.get('email')
        name = request_body.get('name')
        job_title = request_body.get('job_title')
        phone_number = request_body.get('phone_number')
        date_registered: datetime = datetime.now()
        access_level = 'Regular user'

        print(user_id)
        print(username)
        print(email)

        userToAdd.user_id = user_id

        response = userToAdd.signup(user_id=user_id, username=username, password=password, email=email, name=name, job_title=job_title, phone_number=phone_number, date_registered=date_registered, access_level=access_level)
        return response 
    except Exception as e:
        raise Responses.EXCEPTION




