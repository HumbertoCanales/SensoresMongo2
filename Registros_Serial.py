import pickle
from Sensor import Sensor

class Registros_Serial:
    def addRegistro(self, colection, sensor):
        query = self.verRegistros(sensor.nombre)
        registros = query if query else []
        registros.append(Sensor(sensor.nombre, sensor.valor, sensor.fecha))
        fichero = open(sensor.nombre+".pckl", 'wb')
        pickle.dump(registros, fichero)
        fichero.close()

    def verRegistros(self, nombre_sensor):
        fichero = open(nombre_sensor+".pckl", 'ab+')
        fichero.seek(0)
        try:
            registros = pickle.load(fichero)
            return list(registros)
        except:
            return None
        finally:
            fichero.close()