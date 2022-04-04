from xml.sax.saxutils import prepare_input_source


class Celular ():

    def __init__(self):    #definicion del constructor 

    #Estas son las propiedades que tendria el celular
        self.brand="Apple"
        self.color="Blanco"
        self.camara=True   
        self.estado=False   #todos los coches van a estar apagados al pricipio
   

    #Dificion de los comportamientos o metodos que tendran 

    def features(self):
        print("El celular es marca", self.brand, "y es color ", self.color )

    
    def encender(self,estado_celular):
            self.estado=estado_celular
            if self.estado:
                chequeo=self.verificacion()
        
            if chequeo and self.estado:
                print("Celular encendido")

    def verificacion(self):
        print("iniciando celular")
        
        self.bateria="ok"
        self.SO="ok"
        self.display="ok"

        if(self.bateria=="ok" and self.SO=="ok" and self.display=="ok"):
            return True
        else:
            return False


myphone=Celular()

myphone.features()
myphone.encender(True)

