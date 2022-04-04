# def tabla_de_multiplicar(n):
#     for i in range(1,11):
#         print(n,'x', i, '=', i*n)


# tabla_de_multiplicar(5)

# def cadena():
#     return "curso de python"

# print(cadena()) 

# n=5

# def funcion():
#     print(n)
# funcion() 


# def dato():
#     n=2
#     print(n)

# dato()

# n=4
# dato()
# print(n)


# def suma(a,b):   #llama cierta operacion y hace una ejeccion
#     return a+b     

# respuesta= suma(3,4)
# print(respuesta)

#separar una lista en pares e impares 

# ejemplo = [3,4,5,6,7,8,9]

# def separarlista(lista):
#     lista.sort()
#     pares = []
#     impares = []

#     for i in lista:
#         if i % 2 ==0:
#             pares.append(i)
#         else:
#             impares.append(i)

#     return pares,impares

# pares, impares = separarlista(ejemplo)

# print(pares)
# print(impares)


def suma(numero1,numero2):    #se establecen dos valores para usar en la funcion 
    numero3=numero1+numero2     #se usa una variable auxiliar para hacer la suma 
    return numero3              #la funcion regresa un valor 

print(suma(2,3))       #print(numero3)


