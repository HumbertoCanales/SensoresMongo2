import mysql.connector
from mysql.connector import Error
from datetime import datetime as time
from Sensor import Sensor

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
    
    def insert(self, sentencia):
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

    def query(self, sentencia):
        self.__connect__()
        if(self.cur):
            self.cur.execute(sentencia)
            resultado = self.cur.fetchone()
            self.__disconnect__()
            return resultado
        return None
    
    def addRegistro(self, colection, sensor):
        id_sensor, tipo = self.query("SELECT id, tipo_dato FROM sensores WHERE nombre = '"+sensor.nombre+"'")
        self.insert("INSERT INTO valores (sensor_id,"+tipo+", created_at) VALUES ("+str(id_sensor)+","+str(sensor.valor)+", '"+str(sensor.fecha)+"')")

    def verRegistros(self, nombre_sensor):
        try:
            id_sensor, tipo = self.query("SELECT id, tipo_dato FROM sensores WHERE nombre = '"+nombre_sensor+"'")
            registros = self.index("SELECT "+tipo+", created_at FROM valores WHERE sensor_id = '"+str(id_sensor)+"'")
            logs = []
            for registro in registros:
                sensor = Sensor("nombre_sensor", registro[0], registro[1])
                logs.append(sensor)
            return logs
        except:
            return None



