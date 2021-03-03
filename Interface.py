import sys 
import time
from Registros_MySQL import Registros_MySQL
from Registros_MongoDB import mongo
from Registros_Serial import Registros_Serial
from Sensores import Sensores

class Interface():
    def __init__(self):
        self.db = ""
        self.val = 0
        self.val2 = 0

    def int_input(self):
        while True:
            value = input()
            try:
                value = int(value)
                if value != 0:
                    return value
            except ValueError:
                print("Debes ingresar un número entero y que no sea 0")
    
    def timer(self, secs):
        for _ in range(secs):
            print(".", sep=' ', end='', flush=True)
            time.sleep(1)
        print("\n")

    def menu(self):
        self.sensores = Sensores()
        while self.val != 4:
            self.val2 = 0 
            print("\nElige un método de almacenamiento: \n1 - MySQL\n2 - MongoDB\n3 - Almacenamiento local\n4 - Salir")
            self.val = self.int_input()
            if self.val == 1:
                self.db = Registros_MySQL()
                name = "MySQL"
            elif self.val == 2:
                self.db = mongo()
                name = "MongoDB"
            elif self.val == 3:
                self.db = Registros_Serial()
                name = "Almacenamiento local"
            if self.val != 4:
                while self.val2 != 3:
                    print("\nUsando: [ "+name+" ]\nElige una opción: \n1 - Capturar registros\n2 - Leer registros\n3 - Cambiar de almacenamiento")
                    self.val2 = self.int_input()
                    if self.val2 == 1:
                        self.setValues()
                    elif self.val2 == 2:
                        self.getValues()

    def setValues(self):
        print("Inicializando sensores")
        self.timer(3)
        try:
            while True:
                valores = self.sensores.getValores()
                for sensor in valores:
                    self.db.addRegistro("sensores", sensor)
                    print("[ "+sensor.nombre+" ] -> "+str(sensor.valor))
                print("Leyendo datos en 5 segundos (Pulsa ^C para interrumpir)")
                self.timer(5)
        except KeyboardInterrupt:
            pass
    
    def getValues(self):
        nombre_sensor = input("Ingresa el nombre del sensor: ")
        registros = self.db.verRegistros(nombre_sensor)
        if(registros is not None):
            print("\nRegistros del sensor "+nombre_sensor+":")
            for registro in registros:
                print("Valor: "+str(registro.valor)+" | Fecha: "+str(registro.fecha))
        else:
            print("No hay registros de este sensor")

interface = Interface()
interface.menu()