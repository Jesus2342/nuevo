
#Deficion de las funciones 

from ast import While


def suma(indice1,indice2):
    return indice1+indice2

def divide(indice_div1,indicediv2):
    try:
        return indice_div1/indicediv2

    except:
        print("funicion no valida")

#--------------------------------------------

print("Calculadora de operaciones")

while True:
    
    try:
        num1= int (input("Escriba un numero "))

        num2=int (input("Escriba un segundo numero "))

        break

    except ValueError:
        print("los valores de entrada no son validos ")


operac= input("escriba su operacion ")


if operac=="S":
    print(suma(num1,num2))

elif operac=="D":
    print(divide(num1,num2))










