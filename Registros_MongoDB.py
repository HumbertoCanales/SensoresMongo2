import Sensores as s
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
    
    def verDatos(self, colection):
        self.__connect__()
        c = self.db[colection]
        cursor = c.find()
        return cursor
    
    def addRegistro(self, colection, sensor):
        document = sensor.getDocument()
        self.__connect__()
        col = self.db[colection]
        x=col.insert(document)
        return x
    
    def verValores(self,colection,valores):
        for val in self.verDatos(colection):
            print(val)
            '''if('nombre' in val and 'valor' in val and 'tipo' in val):
                sensor=Sensor(val['nombre'],val['valor'],val['tipo'])
                valores.append(sensor)'''
    def verRegistros(self, nombre_sensor):
        pass
            
