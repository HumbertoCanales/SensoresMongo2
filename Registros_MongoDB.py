import Sensores as s
from pymongo import MongoClient
from datetime import datetime as time

class Registros_MongoDB:
    def addRegistro(self, indice):
        v = s.Sensores()
        #print(indice)
        valores = v.getValores()
        temperaturaid = str(indice[0])
        temperatura = valores[1]
        humedadid = str(indice[0])
        humedad = valores[0]
        ultrasonicoid = str(indice[1])
        ultrasonico = valores[3]
        pirid = str(indice[2])
        sPIR = valores[2]
        client = MongoClient("mongodb://127.0.0.1:27017/")
        db = client["Bullsito"]
        bb = db["bb"]
        #bb.insert({"_id": 1, "name":"Abdeel"})
        x = time.now()
        valores = db["Valores"]
        format = x.strftime("%c")
        nid = valores.find().sort("_id",-1).limit(1)
        for x in nid:
            f = int(x["_id"])+1
            #print(f)
            valores.insert({ "_id": f , humedadid: humedad, temperaturaid: temperatura, pirid: sPIR, ultrasonicoid: ultrasonico, "Fecha": format})
        client.close()

