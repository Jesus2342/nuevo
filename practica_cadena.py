edad=input("introduce la edad: ")


while (edad.isdigit()==False):
    print("Selecciona un valor numerico")
    edad=input("introduce la edad: ")


if int (edad)<18:
    print("no puede pasar")

else:
    print("puede pasar")

