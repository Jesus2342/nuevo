class orden_numeros():
     def __init__(self,digitos):
         self.digitos=digitos

     def comprobacion(self):
         if self.digitos=="()":
            print("Combinacion seleccionada",self.digitos)

         if self.digitos=="[]":
             print("Combinacion seleccionada",self.digitos)

         if self.digitos=="{}":
             print("Combinacion seleccionada",self.digitos)
        
         else:
             print("combinacion no encontrada")
    

secuencia=orden_numeros("(")
secuencia.comprobacion()

