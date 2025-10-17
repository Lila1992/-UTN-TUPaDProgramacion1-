#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

#funcion
def hola_mundo():
    print("Hola Mundo!")

# Llamada a la funcion
hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

#funcion
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# llamada a la funcion
print(saludar_usuario(input("introduce tu nombre: ")))

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#funcion
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal 
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

# Llamada a la función con los datos 
informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como 
# parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y 
# devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas 
# funciones para mostrar los resultados.

#funcion 1
import math
def area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area
#funcion 2
def perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro
#programa pricipal
radio = float(input("Ingrese el radio: "))
area_resultado = area_circulo(radio)
perimetro_resultado = perimetro_circulo(radio)

print(f"el area de un circulo es {area_resultado:.2f}") 
print(f"el perimetro es {perimetro_resultado:.2f}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#funcion
def segundos_a_horas(segundos):
  return segundos / 3600

#programa principal
entrada_segundos = float(input("Ingrese la cantidad de segundos a convertir: "))

resultado_horas = segundos_a_horas(entrada_segundos)

print(f"{entrada_segundos} segundos equivalen a {resultado_horas} horas.")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

#funcion
def tabla_multiplicar(numero):
  print(f"\n--- Tabla de Multiplicar del {numero} ---")
  
  #bucle for para iterar desde 1 hasta 10
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# programa principal
numero_usuario = int(input("Ingrese el número cuya tabla de multiplicar desea ver: "))
tabla_multiplicar(numero_usuario)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#funcion
def operaciones_basicas(a, b):
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  division = a / b  
  return (suma, resta, multiplicacion, division)

#programa principal
num1 = float(input("Ingrese el primer número (a): "))
num2 = float(input("Ingrese el segundo número (b): "))

resultados = operaciones_basicas(num1, num2)

print("\n--- Resultados de las Operaciones Básicas ---")
print(f"Suma:          {num1} + {num2} = {resultados[0]}")
print(f"Resta:         {num1} - {num2} = {resultados[1]}")
print(f"Multiplicación: {num1} * {num2} = {resultados[2]}")
print(f"División:      {num1} / {num2} = {resultados[3]}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#funcion
def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  return imc

#programa principal
peso_kg = float(input("Ingrese su peso en kilogramos (ej: 70.5): "))
altura_m = float(input("Ingrese su altura en metros (ej: 1.75): "))

resultado_imc = calcular_imc(peso_kg, altura_m)

print(f"\nSu Índice de Masa Corporal (IMC) es: {resultado_imc:.2f}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 #una temperatura en grados Celsius y devuelva su equivalente en
 #Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 #resultado usando la función

#funcion
def celsius_a_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# programa principal
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

print(f"\n{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F.")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 #tres números como parámetros y devuelva el promedio de ellos.
 #Solicitar los números al usuario y mostrar el resultado usando esta
 #función

#funcion
def calcular_promedio(a, b, c):
  promedio = (a + b + c) / 3
  return promedio

# programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

resultado_promedio = calcular_promedio(num1, num2, num3)

print(f"\nEl promedio de {num1}, {num2} y {num3} es: {resultado_promedio:.2f}")
