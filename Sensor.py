class Sensor():
    def __init__(self,nombre,valor,tipo,Fecha):
        self.nombre=nombre
        self.valor=valor
        self.tipo=tipo
        self.fecha=Fecha

    def getDocument(self):
        document = {
            "nombre":self.nombre,
            "valor":self.valor,
            "tipo":self.tipo,
            "fecha":self.fecha
        }
        return document

    def getTupla(self):
        return (self.nombre,self.valor,self.tipo,self.fecha)
