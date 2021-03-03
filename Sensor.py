class Sensor():
    def __init__(self,nombre,valor,Fecha):
        self.nombre=nombre
        self.valor=valor
        self.fecha=Fecha

    def getDocument(self):
        document = {
            "nombre":self.nombre,
            "valor":self.valor,
            "fecha":self.fecha
        }
        return document

    def getTupla(self):
        return (self.nombre,self.valor,self.fecha)
