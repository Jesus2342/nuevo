
class Coche ():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class moto():

    def desplazamiento(self):

        print("Me desplazo en dos ruedas")


class Camion ():
    def desplazamiento(self):
        print("Me desplazo usando seis ruedas")


def desplazamiento(vehiculo):
    vehiculo.desplazamiento()


vehiculo3=Camion()

desplazamiento(vehiculo3)