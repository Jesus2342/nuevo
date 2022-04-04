#ingresar una direccion de correo electronico pero si fallas 3 veces desplegar la cuenta se ha bloqueado.

email=input("Ingrese su direccion de correo electronico: ")
trials=0

if trials<3:
    print("Gracias por su participacion. Usuario agregado")

for i in email:

    while i!="@":
        print("correo no valido")
        email=input("Ingrese nuevamente su direccion de correo electronico: ")
        
        if i!="@":
            trials=trials+1

        if trials==3:
            print("Cuenta bloqueada")
            break





        




