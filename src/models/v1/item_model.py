from datetime import datetime, timedelta

class Item(object):
    
    def __init__(self) -> None:
        self.sku : str = None
        self.item_name : str = None
        self.item_location : str = None
        self.last_updated : datetime.now()
        self.quantity_counted : int = None

    def toJSON(self):
        return {
            "sku": self.sku,
            "item_name" : self.item_name,
            "last_updated" : self.last_updated,
            "quantity_counted" : self.quantity_counted
        }