#EJERCICIO 1
for num in range(1, 101):
    print(num)      

#EJERCICIO 2=
numero = int(input("Introduce un número: "))
contador = 0

if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10 
        contador += 1

print(f"Tiene {contador} dígitos.")

#Ejercicio 3
numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

suma = 0
bandera = True

for i in range(numero_1 + 1, numero_2): 
    suma = suma + i
    
print(suma)

#ejercicio 4
total = 0
numero = 1
while numero != 0:
    numero = int(input("Ingresa un número entero (ingresa 0 para terminar): "))
    total += numero
print(f"La suma total es: {total}")

#ejercicio 5
import random

for i in range(1):
    numero_secreto = random.randint(0, 9)
    intentos = 0
    
    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 0 y 9.")
    
    suposicion = -1
    
    while suposicion != numero_secreto:
        suposicion = int(input("Ingresa tu suposición: "))
        intentos += 1
        
        if suposicion < numero_secreto:
            print("El número secreto es más grande. Inténtalo de nuevo.")
        elif suposicion > numero_secreto:
            print("El número secreto es más pequeño. Inténtalo de nuevo.")
    
    print(f"¡Felicitaciones! Adivinaste el número {numero_secreto}.")
    print(f"Te tomó {intentos} intentos para acertar.")

    #ejercicio 6
print("Números pares del 100 al 0:")
numero = 100
while numero >= 0:
    print(numero)
    numero = numero - 2

    #ejercicio 7
numero_limite = int(input("Ingresa un número entero positivo: "))
suma = 0
for i in range(numero_limite + 1):
    suma += i
print(f"La suma de los números de 0 a {numero_limite} es: {suma}")

#ejercicio 8
print(f"Por favor, ingresa {cantidad_de_numeros} números enteros.")

for i in range(cantidad_de_numeros):
    numero = int(input(f"Ingresa el número #{i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
        
print("\n--- Resultados del análisis ---")
print(f"Total de números pares: {pares}")
print(f"Total de números impares: {impares}")
print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")

#ejercicio 9
cantidad_de_numeros = 100
suma = 0
contador = 0

print(f"Por favor, ingresa {cantidad_de_numeros} números enteros.")

while contador < cantidad_de_numeros:
    numero = int(input(f"Ingresa el número #{contador + 1}: "))
    suma += numero
    contador += 1

if cantidad_de_numeros > 0:
    media = suma / cantidad_de_numeros
    print(f"\nLa media de los {cantidad_de_numeros} números es: {media:.2f}")
else:
    print("\nNo se ingresaron números para calcular la media.")
    
    #ejercicio 10
numero_como_texto = input("Ingresa un número para invertir: ")

numero_invertido = numero_como_texto[::-1]

print(f"El número invertido es: {numero_invertido}")
