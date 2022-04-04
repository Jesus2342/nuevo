class Coche():


    def __init__(self):    #definicion del constructor 

    #Estas son las propiedades que tendria el carro
     self.largo=250
     self.ancho=120
     self.__ruedas=4   #variable encapsulada (no sera accesible fuera de la clase)
     self.enmarcha=False   #todos los coches van a estar parados al pricipio
   
    
    
    #vamos a establecer los comportamientos o metodos 
    #Los metodos se crean apatir de def 

    def arrancar (self):
        self.enmarcha=True   #quiero cambiar el estado del automovil

    def estado(self):

        if(self.enmarcha):
            return "el coche esta en marcha"
        
        
        else:
            return "el coche esta parado"

    def estado_actual(self,acelerar):
        self.enmarcha=acelerar

        if(self.enmarcha):
            chequeo=self.rev_interna()

        if(self.enmarcha and chequeo):
            print("encendido") 

        elif(self.enmarcha and chequeo==False):
            print("coche no puede arrancar, el chequeo interno fallo")
        else:
            print("apagado")


    def features(self):
        print("El coche tiene un largo de  ", self.largo, "un ancho de ", self.ancho, "y un numero de ruedas de ", self.__ruedas)



    def rev_interna(self):
        print("realizando revision interna")

        self.gasoina="ok"
        self.aceite="ok"
        self.agua="ok"

        if self.gasoina=="ok" and self.aceite=="ok" and self.aceite=="ok":
            return True
        
        else:
            return False

#primero tenemos que salir de la clase para poder crear un objeto 
miCoche=Coche()   #intanciacion de clase
miCoche2=Coche()

#ahora si me interesara ver la longitud y el largo de mi objeto
#print("El largo del coche es", miCoche.ancho)

#print("El coche tiene ", miCoche.ruedas,"ruedas")

print("El coche 1 tiene las siguientes caracteristicas")
miCoche.features()

print("Su estado acutual es")
print(miCoche.estado_actual(True))

#-----------------------------------------------------------------------
print("-----A continuacion creamos el objeto 2 ")

print("El coche 2 tiene las siguientes caracteristicas")
miCoche2.features()

print("Su estado acutual es")
print(miCoche2.estado_actual(False))