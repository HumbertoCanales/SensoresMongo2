import mysql.connector
from mysql.connector import Error
from datetime import datetime as time
import Registros_MongoDB

class Registros_MySQL:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "admin"
        self.password = "123"
        self.db = "Bullsito"

    def __connect__(self):
        try:
            self.con = mysql.connector.connect(host=self.host, user=self.user, password=self.password, db=self.db)
            if self.con.is_connected():
                print("Conexión exitosa!")
                self.cur = self.con.cursor()
        except Error as ex:
            print("Error al conectar: "+ex)

    def __disconnect__(self):
        self.cur.close()
        self.con.close()
    
    def insertarRegistro(self, sentencia):
        self.__connect__()
        self.cur.execute(sentencia)
        self.con.commit()
        rows = self.cur.rowcount
        self.__disconnect__()
        return rows

    def consulta(self, sentencia):
        self.__connect__()
        self.cur.execute(sentencia)
        resultados = self.cur.fetchall()
        self.__disconnect__()
        return list(resultados)
    
    def addRegistro(self, id_sensor, tipo, valor):
        self.insertarRegistro("INSERT INTO valores (sensor_id,"+tipo+") VALUES ("+id_sensor+","+valor+")")




