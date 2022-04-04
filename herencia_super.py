class persona():
    
    def __init__(self, nombre, edad, lugar_residencia):


        self.nombre=nombre 
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion (self):
            print("nombre ", self.nombre, "Edad", self.edad, "lugar residencia", self.lugar_residencia)


class empleado(persona):

     def __init__(self, salario, antiguedad, nombre_empleado, edad_emepleado, ciudad_empleado):
         super().__init__(nombre_empleado, edad_emepleado, ciudad_empleado)
         self.salario=salario
         self.antiguedad=antiguedad

        

antonio=persona("antonio", 32, "españad")
#purbea git
antonio.descripcion()