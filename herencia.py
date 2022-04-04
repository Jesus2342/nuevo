class vehiculos():

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False   #cuando contruimos un objeto por defecto no va a estar en marcha  
        self.acelera=False    
        self.frena=False


    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("La Marca es ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha", self.enmarcha, "\Acelerando", self.acelera, "\nFrenando ", self.frena)


class Moto(vehiculos):


    def caballito(self):
        print("hacer caballito")

class Furgoneta(vehiculos):
    def carga(self,cargar):
        self.cargado=cargar

        if self.cargado:
            print("furgoneta cargada")

        else:
            print("no esta cargada")

class Velectricos():
    def __init__(self):
        self.autonomia=100


    def estado_pila(self):
        self.carga=True

        if(self.carga):
            print("bateria cargada")

        else:
            print("bateria baja")

    
class Bici_electrica(Velectricos,vehiculos):
    pass

moto_honda=Moto("Honda", "CBR")
moto_honda.estado()
moto_honda.caballito()

camioneta=Furgoneta("Chevroleta", "crv")

camioneta.estado()
camioneta.acelerar()
camioneta.carga(True)

electrico=Velectricos()

electrico.estado_pila()

mibici=Bici_electrica()


 
 