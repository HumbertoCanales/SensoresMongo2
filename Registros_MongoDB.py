import Sensores as s
from pymongo import MongoClient
from datetime import datetime as time

class mongo:
    try:
        connect = MongoClient("mongodb://localhost:27017/")
        db= connect["Sensores"]
    except:
        print("Could not connect to MongoDB")
    
    def verDatos(self, colection):
        c = self.db[colection]
        cursor = c.find()
        return cursor
    
    def addRegistro(self, colection, document):
        col = self.db[colection]
        x=col.insert_one(document)
        return x.inserted_id

