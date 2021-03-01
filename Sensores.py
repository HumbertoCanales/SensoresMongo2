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
    
    def getPIR(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(21, GPIO.IN)
        pir = GPIO.input(21)
        self.arreglo.append({"nombre": "PIR", "valor": pir, "tipo": "boleano"})
        GPIO.cleanup()

    def getUltrasonico(self):
        TRIG = 23
        ECHO = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        try:
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            time.sleep(2)
            GPIO.output(TRIG, GPIO.LOW)
            pulso_inicio = time.time()
            pulso_fin = time.time()
            while GPIO.input(ECHO) == 0:
               pulso_inicio = time.time()
            while GPIO.input(ECHO) == 1:
               pulso_fin = time.time()
            duracion = pulso_fin - pulso_inicio
            distancia = (34300 * duracion) / 2
            self.arreglo.append({"nombre": "ultrasonico", "valor": distancia, "tipo": "flotante"})
        except RuntimeError as error:
            print("Error: " + error)
        GPIO.cleanup()

    def getTempHum(self):
        pin = 4
        i = 0
        while i <= 5:
            i += 1
            try:
                humedad, temperatura = adafruit_dht.read(11, pin)
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
