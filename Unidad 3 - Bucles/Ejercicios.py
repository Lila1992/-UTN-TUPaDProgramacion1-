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
        numero = numero // 10 # 321 32 3  
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