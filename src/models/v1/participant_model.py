## This is the sub model that we need for updating quantity counted by the specified user_id

class Participant(object):
    
    def __init__(self) -> None:
        self.user_id : str = None
        self.username : str = None
        self.quantity_counted : int = None
        self.email : str = None