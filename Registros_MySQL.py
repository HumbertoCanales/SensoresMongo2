import mysql.connector
from mysql.connector import Error
from datetime import datetime as time
import Registros_MongoDB

class Registros_MySQL:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = ""
        self.db = "sensores_py"

    def __connect__(self):
        try:
            self.con = mysql.connector.connect(host=self.host, user=self.user, password=self.password, db=self.db)
            if self.con.is_connected():
                self.cur = self.con.cursor()
        except Error as ex:
            print("Error al conectar: ", ex)
            self.cur = None

    def __disconnect__(self):
        self.cur.close()
        self.con.close()
    
    def insertarRegistro(self, sentencia):
        self.__connect__()
        if(self.cur):
            self.cur.execute(sentencia)
            self.con.commit()
            rows = self.cur.rowcount
            self.__disconnect__()
            return rows
        return None

    def index(self, sentencia):
        self.__connect__()
        if(self.cur):
            self.cur.execute(sentencia)
            resultados = self.cur.fetchall()
            self.__disconnect__()
            return list(resultados)
        return None

    def consulta(self, sentencia):
        self.__connect__()
        if(self.cur):
            self.cur.execute(sentencia)
            resultado = self.cur.fetchone()
            self.__disconnect__()
            return resultado
        return None
    
    def addRegistro(self, colection, sensor):
        id_sensor, tipo = self.consulta("SELECT id, tipo_dato FROM sensores WHERE nombre = '"+sensor.nombre+"'")
        self.insertarRegistro("INSERT INTO valores (sensor_id,"+tipo+") VALUES ("+str(id_sensor)+","+str(sensor.valor)+")")

    def verRegistros(self, nombre_sensor):
        try:
            id_sensor, tipo = self.consulta("SELECT id, tipo_dato FROM sensores WHERE nombre = '"+nombre_sensor+"'")
            registros = self.index("SELECT "+tipo+" FROM valores WHERE sensor_id = '"+str(id_sensor)+"'")
            logs = []
            for registro in registros:
                logs.append(registro[0])
            return logs
        except:
            return None



