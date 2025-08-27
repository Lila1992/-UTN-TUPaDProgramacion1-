edad = int(input("ingrese su edad "))
if edad < 12:
    print("Niño/a")
if edad >= 12 and edad < 18:
    print("Adolescente")
if edad >= 18 and edad < 30:
    print("Adulto/a joven")
if edad >= 30:
    print("Adulto/a")
else:
    print("no corresponde")
