from src.services.database import MongoDB

import src.globalvars as globalvars

MongoDBConnection = MongoDB( connectionString= globalvars.CONST_MONGO_URL, dataBaseName= globalvars.CONST_DATABASE)
MongoDBConnection.connect()