import uuid, datetime, random, bcrypt, re
from itertools import cycle

def generate_new_inventory_uuid() -> str :
  inventoryId = str(uuid.uuid4().hex)

  return inventoryId


def generate_new_user_uuid() -> str :
  userId = str(uuid.uuid4().hex)

  return userId



def generate_hash_password(password) -> str:
  salt = bcrypt.gensalt()
  hashedPassword = bcrypt.hashpw(password.encode("utf-8"), salt )

  return hashedPassword