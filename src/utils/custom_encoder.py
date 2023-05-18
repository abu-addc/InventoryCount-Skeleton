import json
from datetime import datetime
from bson import ObjectId

# Custom JSONEncoder to handle serialization of ObjectId and datetime objects
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)