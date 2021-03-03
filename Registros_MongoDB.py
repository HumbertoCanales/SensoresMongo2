from pymongo import MongoClient
from pymongo import errors as mongoerrors
from datetime import datetime as time
from Sensor import Sensor

class mongo:
    def __init__(self):
        self.client = "mongodb://localhost:27017/"
        self.database = "Actividad"
    
    def __connect__(self):
        try:
            self.connect = MongoClient(self.client)
            self.db = self.connect[self.database]
        except mongoerrors.OperationFailure as e:
            print("Could not connect to MongoDB")
            print(e.code)
            print(e.details)
    
    def verDatos(self, colection, parametro={}):
        self.__connect__()
        c = self.db[colection]
        cursor = c.find(parametro)
        return cursor
    
    def addRegistro(self, colection, sensor):
        document = sensor.getDocument()
        self.__connect__()
        col = self.db[colection]
        x = col.insert(document)
        return x
    
    def verRegistros(self, nombre_sensor):
        try:
            myquery={"nombre":nombre_sensor}
            registros = self.verDatos("sensores",myquery)
            logs = []
            for registro in registros:
                sensor = Sensor("nombre_sensor", registro['valor'], registro['fecha'])
                logs.append(sensor)
            return logs
        except:
            return None
            
