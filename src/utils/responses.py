from enum import Enum
class Responses(Enum):
    SUCCESS = 1
    FAIL = 2
    UNAUTHORIZED = 3 
    
    INVENTORY_NOT_FOUND = 10

    REQUIRED_FIELDS_MISSING = 430

    EXCEPTION = 999