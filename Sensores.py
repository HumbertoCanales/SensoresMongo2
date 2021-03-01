import Adafruit_DHT as adafruit_dht
import  RPi.GPIO as GPIO
import time

class Sensores():
    def __init__(self):
        self.ultrasonico = 0
        self.temperatura = 0
        self.humedad = 0
        self.pir = 0
        self.arreglo = []
        self.PIN_TRIG = 23
        self.PIN_ECHO = 24
        self.PIN_PIR = 21
        self.PIN_DHT = 4
        GPIO.setmode(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_PIR, GPIO.IN)
        GPIO.setup(self.PIN_TRIG, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
    
    def getPIR(self):
        pir = GPIO.input(21)
        self.arreglo.append({"nombre": "PIR", "valor": pir, "tipo": "boleano"})
        GPIO.cleanup()

    def getUltrasonico(self):
        try:
            GPIO.output(self.PIN_TRIG, True)
            time.sleep(0.00001)
            GPIO.output(self.PIN_TRIG, False)
            while GPIO.input(self.PIN_ECHO) == 0:
               pulso_inicio = time.time()
            while GPIO.input(self.PIN_ECHO) == 1:
               pulso_fin = time.time()
            duracion = pulso_fin - pulso_inicio
            distancia = (34300 * duracion) / 2
            self.arreglo.append({"nombre": "ultrasonico", "valor": distancia, "tipo": "flotante"})
        except RuntimeError as error:
            print("Error: " + error)
        GPIO.cleanup()

    def getTempHum(self):
        i = 0
        while i <= 5:
            i += 1
            try:
                humedad, temperatura = adafruit_dht.read(11, self.PIN_DHT)
                if humedad is not None and temperatura is not None:
                    self.arreglo.append({"nombre": "temperatura", "valor": temperatura, "tipo": "flotante"})
                    self.arreglo.append({"nombre": "humedad", "valor": humedad, "tipo": "flotante"})
                    break
            except RuntimeError as error:
                print("Error: " + error)
            
    def getValores(self):
        self.arreglo = []
        self.getPIR()
        self.getUltrasonico()
        self.getTempHum()
        return self.arreglo
