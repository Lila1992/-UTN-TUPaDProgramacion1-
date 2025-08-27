nombre = input("ingrese su nombre")
numero = int(input("ingrese un numero"))
if numero == 1:
    print(nombre.upper())
elif numero == 2:
    print(nombre.lower())
elif numero == 3:
    print(nombre.capitalize())
else:
    print("numero incorrecto")