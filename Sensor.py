class Sensor():
    def __init__(self,nombre,valor,tipo):
        self.nombre=nombre
        self.valor=valor
        self.tipo=tipo

    def getDocument(self):
        document = {
            "nombre":self.nombre,
            "valor":self.valor,
            "tipo":self.tipo
        }
        return document