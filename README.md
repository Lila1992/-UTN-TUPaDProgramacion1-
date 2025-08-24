# -UTN-TUPaDProgramacion1-
#ejercicio 1
print("hola mundo") 

#ejercicio 2
nombre = input("ingrese nombre")
print("hola {nombre} como estas")

#ejercicio3
nombre = input("ingrese su nombre")
apellido = input("ingrese su apellido")
edad = input("ingrese su edad")
lugar_de_residencia = input("ingrese su lugar de residencia")
print(f"soy {nombre}, {apellido} tengo {edad} años y vivo en {lugar_de_residencia}")

#ejercicio4
import math
radio_circulo = float(input("ingrese el valor de radio del circulo"))
area_circulo = math.pi * (radio_circulo)**2
perimetro_circulo = 2 * math.pi * radio_circulo
print(f"el areas es  {area_circulo} y el perimetro es {perimetro_circulo}")

#ejercicio5
cant_segundos = float(input("ingrese la cantidad de segundos"))
cant_horas= round(cant_segundos / 3600, 2)
print(f"la cantidad de segundos equivale a {cant_segundos} son {cant_horas} horas")

#ejercicio6
num: int=int(input("ingrese numero de su tabla"))
print  (num ,"x 1= ", num*1)
print  (num ,"x 2= ", num*2)
print  (num ,"x 3= ", num*3)
print  (num ,"x 4= ", num*4)
print  (num ,"x 5= ", num*5)
print  (num ,"x 6= ", num*6)
print  (num ,"x 7= ", num*7)
print  (num ,"x 8= ", num*8)
print  (num ,"x 9= ", num*9)
print  (num ,"x 10= ", num*10)

#ejercicio7
num1 = float (input("ingrese el primer numero, distinto de 0"))
num2 = float (input("ingrese el segundo numero, distinto de 0"))
print("la suma de ", num1, "y ", num2, "es", num1+num2)
print("la resta de ", num1, "y ", num2, "es", num1-num2)
print("la multiplicacion de ", num1, "y ", num2, "es", num1*num2)
print("la division de ", num1, "y ", num2, "es", num1/num2)

#ejercicio8
peso = float(input("ingrese su peso"))
altura = float(input("ingrese altura"))
masaCorporal= round(peso/altura**2, 2)
print("su IMC es", masaCorporal)

#ejercicio9
temp_celsius = float(input("ingrese temperatura en grados celsius"))
temp_far = round((9/5) * temp_celsius + 32, 2)
print (f" {temp_celsius} grados celcius equivalen a {temp_far} grados fahrenheit")

#ejecicio10
numero_a = float(input("ingrese primer numero"))
numero_b = float(input("ingrese segundo numero"))
numero_c = float(input("ingrese tercer numero"))
suma_a_b_c = numero_a + numero_b + numero_c
prom_a_b_c = round((suma_a_b_c)/3, 2)
print ("su promedio entre es:  {prom_a_b_c}") s
