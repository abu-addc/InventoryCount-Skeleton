from datetime import datetime, timedelta

class Item(object):
    
    def __init__(self) -> None:
        self.sku : str = None
        self.item_name : str = None
        self.last_updated : datetime.now()
        self.quantity_counted : int = None