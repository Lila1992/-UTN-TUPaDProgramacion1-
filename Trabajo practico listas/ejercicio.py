#ejercicio 1: Crear una lista con las notas de 10 estudiantes.
#• Mostrar la lista completa.
#• Calcular y mostrar el promedio.
#• Indicar la nota más alta y la más baja.

notas = [8.5, 7.0, 9.2, 6.5, 5.0, 10.0, 7.8, 8.0, 9.5, 6.0]
print("Lista completa de notas:")
for nota in notas:
    print(nota)

suma_notas = 0
for nota in notas:
    suma_notas += nota

promedio = suma_notas / len(notas)
print(f"\nEl promedio de las notas es: {promedio:.2f}")

nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print(f"\nLa nota más alta es: {nota_mas_alta}")
print(f"La nota más baja es: {nota_mas_baja}")

#ejercicio 2: Pedir al usuario que cargue 5 productos en una lista.
#• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#• Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i + 1} de 5: ")
    productos.append(producto)

productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
for producto in productos_ordenados:
    print(producto)

producto_a_eliminar = input("\n¿Qué producto desea eliminar de la lista? ")

productos.remove(producto_a_eliminar)
print("\nEl producto ha sido eliminado.")

print("La lista de productos actualizada es:")
for producto in productos:
    print(producto)

#ejercicio 3: Generar una lista con 15 números enteros al azar entre 1 y 100.
#• Crear una lista con los pares y otra con los impares.
#• Mostrar cuántos números tiene cada lista.

import random
numeros_al_azar = []

for _ in range(15):
    numeros_al_azar.append(random.randint(1, 100))
    print(f"la lista original es: {numeros_al_azar}")

numeros_pares = []
numeros_impares = []

for numero in numeros_al_azar:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)


print(f"Lista de numeros pares: {numeros_pares}")
print(f"Lista de numeros impares {numeros_impares}")

print(f"cantidad de numeros pares: {len(numeros_pares)}")
print(f"cantidad de numeros impares {len(numeros_impares)}")

#ejercicio 4: Dada una lista con valores repetidos:
# datos = [1,3,5,3,7,1,9,5,3]
#• Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]
print(f"La lista original es {datos}")

conjunto_sin_duplicados = set(datos)
lista_sin_duplicados = list(conjunto_sin_duplicados)
print(f"la lista sin elementos repetidos es: {lista_sin_duplicados}")

#ejercicio 5: Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada

estudiantes = ["lila", "ramiro", "lucas", "cristina", "agostina", "ciro", "sebastian", "ana"]
print(estudiantes)
continuar = True
while continuar:
    accion = input("n/¿Quieres agregar un estudiante (a), elimimar un estudiantes (e) o salir (s)").lower()
    if accion == "a":
        nuevo_estudiante = input("ingrese el nombre del nuevo estudiante")
        estudiantes.append(nuevo_estudiante)
        print(f"{nuevo_estudiante} ha sido agregado a la lista")
    elif accion == "e":
        estudiante_eliminado = input("ingrese el nombre del estudiante a eliminar")
        if estudiante_eliminado in estudiantes:
            estudiantes.remove(estudiante_eliminado)
            print(f"{estudiante_eliminado} ha sido eliminado de la lista")
        else:
            print(f"error el {estudiante_eliminado} no existe en la lista")

    elif accion == "s":
        print("saliendo")
        continuar = False
    else: 
         print("opcion no valida. por favor ingrese (a), (e), o (s)")

print("n/La lista final de estudiantes es")
for estudiante in estudiantes:
    print(estudiante)

#ejercicio 6: Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).

numeros = [1,2,3,4,5,6,7]
print(f"lista original: {numeros}")
ultimo_elemento = numeros.pop()
numeros.insert(0,ultimo_elemento)
print(f"lista rotada: {numeros}")

#ejercicio 7: Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
#semana.
#•Calcular el promedio de las mínimas y el de las máximas.
#• Mostrar en qué día se registró la mayor amplitud térmica.

#matriz temperaturas de la semana 
#[min, max]
temperaturas = [
    [29, 30], #lunes
    [25, 29], #martes
    [28, 35], #miercoles
    [15, 25], #jueves
    [30, 37], #viernes
    [19, 29], #sabado
    [29, 36], #domingo
]
print(temperaturas)

suma_minimas = 0
suma_maximas = 0

for dia in temperaturas:
    suma_minimas += dia[0]
    suma_maximas += dia[1]
    num_dias = len(temperaturas)
    promedio_minimas = suma_minimas / num_dias
    promedio_maximas = suma_maximas / num_dias
    print(f"el promedio de las temperaturas minimas es {promedio_minimas:.2f}°c")
    print(f"el promedio de las temperaturas maximas es {promedio_maximas:.2f}°c")

dias_semana = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado","domingo"]
mayor_amplitud = 0
dia_mayor_amplitud = ""
for i, dia in enumerate(temperaturas):
    amplitud_termica = dia[1] - dia[0]
    if amplitud_termica > mayor_amplitud:
        mayor_amplitud = amplitud_termica
        dia_mayor_amplitud = dias_semana[i]
print(f"\nla mayor amplitud termica fue: {mayor_amplitud}°c, y se registro el dia: {dia_mayor_amplitud}")

#ejercicio 8: Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia

#matriz de notas
notas = [
    [7.5 , 8.0 , 9.0], #nota estudiante 1
    [6.0 , 7.5 , 8.5], #nota estudiante 2
    [9.0 , 9.5 , 8.0], #nota estudiante 3
    [5.0 , 6.5 , 7.0], #nota estudiante 4
    [1.5 , 5.0 , 9.5], #nota estudiante 5
]
print("promedio de cada estudiante: ")
for i in range(len(notas)):
    suma_notas_estudiante = sum(notas[i])
    promedio_estudiante = suma_notas_estudiante / len(notas[i])
    print(f"estudiante {i + 1}: {promedio_estudiante:.2f}")

num_materias = len(notas[0])
print("\npromedio de cada materia ")
for j in range(num_materias):
    suma_notas_materia = 0
    for i in range(len(notas)):
        suma_notas_materias += notas [i][j]
    promedio_materia = suma_notas_materia / len(notas)
    print (f"materia {j + 1}: {promedio_materia:.2f}")

#ejercicio 9: Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

tablero = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))

jugador_actual = "X"
jugadas = 0
while jugadas < 9:
    mostrar_tablero(tablero)
    print(f"\nturno del jugador {jugador_actual}")
    
    fila_valida = False
    while not fila_valida:
        fila_str = input("ingresa la fila (0, 1 O 2):")
        if fila_str.isdigit() and 0 <= int(fila_str) < 3:
            fila = int(fila_str)
            fila_valida = True
        else:
            print("entrada no valida. ingresa un numero del 0 al 2")

    columna_valida = False
    while not columna_valida:
        columna_str = input("ingresa columna (0, 1 O 2):")
        if columna_str.isdigit() and 0 <= int(columna_str) < 3:
            columna = int(fila_str)
            columna = True
        else:
            print("entrada no valida. ingresa un numero del 0 al 2")
    if tablero[fila][columna] == "_":
        tablero[fila][columna] = jugador_actual
        jugadas += 1
        if jugador_actual =="X":
           jugador_actual = "O"
        else:
            jugador_actual = "X"
    else:
        print("esa posicion ya esta ocupada intente de nuevo")
print("\njuego terminado")
mostrar_tablero(tablero)

#ejercicio 10: Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.

# Matriz de 4x7 con las ventas de 4 productos durante 7 días
ventas = [
    [10, 15, 20, 12, 18, 25, 30],  # Producto 1
    [5, 8, 12, 10, 15, 18, 22],   # Producto 2
    [25, 20, 15, 30, 22, 18, 10], # Producto 3
    [15, 12, 18, 20, 25, 10, 5]   # Producto 4
]
print("Total vendido por cada producto:")
for i, fila in enumerate(ventas):
    total_producto = sum(fila)
 
print(f"Producto {i + 1}: {total_producto}")

ventas_por_dia = [0] * 7 

#ventas por día
for fila in ventas:
    for dia, venta in enumerate(fila):
        ventas_por_dia[dia] += venta

#venta máxima y su índice
max_venta_dia = max(ventas_por_dia)
dia_con_mas_ventas = ventas_por_dia.index(max_venta_dia) + 1 # Sumamos 1 para que sea del 1 al 7

print("\nVentas totales por día:", ventas_por_dia)
print(f"El día con mayores ventas totales es el Día {dia_con_mas_ventas} con un total de {max_venta_dia} ventas.")

total_ventas_por_producto = []
for fila in ventas:
    total_ventas_por_producto.append(sum(fila))

#total de ventas más alto y su índice
max_venta_semanal = max(total_ventas_por_producto)
producto_mas_vendido = total_ventas_por_producto.index(max_venta_semanal) + 1

print("\nTotal de ventas por producto en la semana:", total_ventas_por_producto)
print(f"El producto más vendido de la semana es el Producto {producto_mas_vendido} con un total de {max_venta_semanal} ventas.")







