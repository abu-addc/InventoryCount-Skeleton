import os

from dotenv.main import load_dotenv
import os

load_dotenv()

'''DATABASE'''
CONST_MONGO_URL = os.environ.get('CONST_MONGO_URL')
CONST_DATABASE = os.environ.get('CONST_DATABASE')

'''COLLECTIONS'''
INVENTORY_COUNT_COLLECTION = os.getenv('INVENTORY_COUNT_COLLECTION')
USER_COLLECTION = os.getenv('USER_COLLECTION')