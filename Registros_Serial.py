import pickle

class Registros_Serial:
    def addRegistro(self, colection, sensor):
        registros = []
        registros = self.verRegistros(sensor.nombre)
        if(registros is not None):
            registros.append(sensor.getDocument())
            fichero = open(sensor.nombre+".pckl", 'wb')
            pickle.dump(registros, fichero)
            fichero.close()
        else:
            registros = []
            registros.append(sensor.getDocument())
            fichero = open(sensor.nombre+".pckl", 'wb')
            pickle.dump(registros, fichero)
            fichero.close()

    def verRegistros(self, nombre_sensor):
        fichero = open(nombre_sensor+".pckl", 'ab+')
        fichero.seek(0)
        try:
            registros = pickle.load(fichero)
            print(registros)
            return list(registros)
        except:
            print("El fichero está vacío")
            return None
        finally:
            fichero.close()