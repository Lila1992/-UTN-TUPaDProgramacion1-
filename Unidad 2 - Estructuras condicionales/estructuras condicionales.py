#ejercicio 1

edad = int(input("ingrese su edad"))
if edad >= 18:
    print("es mayor de edad")
else:
    print("es menor de edad")

#ejercicio 2

nota = int(input("ingrese su nota"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#ejercicio 3

numero = int(input("ingrese un numero"))
if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es impar")


#ejercicio 4

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

#ejercicio 5

contraseña = (input("ingrese su contraseña "))
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print ("Ha ingresado una contraseña correcta")
else:
    print("por favor ingrese una contraseña de 8 a 14 caracteres")
    
#ejercicio 6

from statistics import mode, median, mean
import random 
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media > mediana and mediana > moda:
    print("sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("sesgo negativo o a la izquierda")
else:
    print("sin sesgo")
    
#ejercicio 7

palabra = input("ingrese una palabra: ")
ultima_letra = len(palabra)
if palabra[ultima_letra-1] == "a":
    print(palabra + "!")
elif palabra[ultima_letra-1] == "e":
    print(palabra + "!")
elif palabra[ultima_letra-1] == "i":
    print(palabra + "!")
elif palabra[ultima_letra-1] == "o":
    print(palabra + "!")
elif palabra[ultima_letra-1] == "u":
    print(palabra + "!")
else:
    print(palabra)
          
 #ejercicio 8

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

#ejercicio 9

magnitud_terremoto = int(input("ingrese la magnitud del terremoto"))
if magnitud_terremoto <= 3:
    print("muy leve, imperceptible")
elif magnitud_terremoto >=3 and magnitud_terremoto <=4:
    print("leve, legeramente perceptible")
elif magnitud_terremoto >=4 and magnitud_terremoto <=5:
    print("moderado, sentido por personas pero generalmente no causa daños")
elif magnitud_terremoto >=5 and magnitud_terremoto <=6:
    print("fuerte, puede causar daños en estructuras debiles")
elif magnitud_terremoto >=6 and magnitud_terremoto <=7:
    print("Muy fuerte, puede causar daños significativos")
else:
    print("Extremo, puede causar graves daños a gran escala")

#ejercicio 10

hemisferio = input("ingrese en que hemisferio se encuentra norte o sur? ").upper()
mes = int(input("que mes del año es? "))
dia = int(input("que dia es? "))
if hemisferio == "norte":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "verano"
else:
        estacion = "otoño"

if hemisferio == "sur":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "invierno"
else:
        estacion = "primavera"
print(f"te encuentras en {estacion}")


