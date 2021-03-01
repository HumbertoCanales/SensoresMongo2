import sys 
import time
from pymongo import MongoClient
#from Registros_MySQL import Registros_MySQL
from Registros_MongoDB import mongo
from Sensores import Sensores

def int_input():
  while True:
    val = input()
    try:
      val = int(val)
      if val != 0:
        return val
    except ValueError:
      print("Debes ingresar un número entero y que no sea 0")

db = ""
val = 0      

def menu():
    print("Elige una base de datos: \n1 - MySQL\n2 - MongoDB")
    val = int_input()
    if val == 1:
        pass
        #db1 = Registros_MySQL()
    elif val == 2:
        db = mongo()
    else:
        print("Opción no encontrada")
        return
    sensores = Sensores()
    val = 0
    while val != 3:
        print("Elige una opción: \n1 -  Añadir registros\n2 - Leer registros\n3 - Salir")
        val = int_input()
        if val == 1:
            time.sleep(3)
            try:
                while True:
                    valores = sensores.getValores()
                    for val in valores:
                        #db.addRegistro(val['nombre'], val['tipo'], val['valor'])
                        db.addRegistro("sensores",val.getDocument())
                        print("Nombre "+val.nombre+" Valor:  "+str(val.valor))
                    print("Leyendo datos en 5 segundos... (Pulsa ^C para interrumpir)")
                    time.sleep(5)
            except KeyboardInterrupt:
                pass
        elif val == 2:
            print("XD")
            valores = sensores.getData()
            db.verValores('sensores',valores)
            for val in valores:
                print("Nombre "+val.nombre+" Valor:  "+str(val.valor))
            valores = []
            #db.leerRegistros()
    
menu()