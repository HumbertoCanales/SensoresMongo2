class Sensor():
    def __init__(self,nombre,valor,tipo):
        self.nombre=nombre
        self.valor=valor

    def getDocument(self):
        document = {
            "nombre":self.nombre,
            "valor":self.valor
        }
        return document

    def getTupla(self):
        return (self.nombre,self.valor)