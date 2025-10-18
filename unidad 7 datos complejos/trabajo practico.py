#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
#1450}
#Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

# 1. Diccionario inicial
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario de precios actualizado:")
print(precios_frutas)

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

# Diccionario punto 1
precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450, 
    'Naranja': 1200, 
    'Manzana': 1500, 
    'Pera': 2300
}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario de precios luego de la actualización:")
print(precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

# Diccionario del punto 1
precios_frutas = {
    'Banana': 1330, 
    'Ananá': 2500, 
    'Melón': 2800, 
    'Uva': 1450, 
    'Naranja': 1200, 
    'Manzana': 1700, 
    'Pera': 2300
}

lista_frutas = list(precios_frutas.keys())

print("Lista de frutas:")
print(lista_frutas)

#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe

def programa_telefonos():
    contactos = {}
    
    print("--- Carga de 5 Contactos ---")
    for i in range(5):
        nombre = input(f"Nombre del contacto {i + 1}: ").lower()
        numero = input(f"Número de {nombre.capitalize()}: ")
        contactos[nombre] = numero
    
    print("\n--- Consulta ---")
    nombre_consulta = input("Buscar nombre: ").lower()
    
    numero = contactos.get(nombre_consulta, "No encontrado")
    
    print(f"\nNúmero de {nombre_consulta.capitalize()}: {numero}")

programa_telefonos()

#5) Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

def analizar_frase():
    frase_entrada = input("Ingrese una frase o un texto: ")
    
    palabras = frase_entrada.lower().split()
    
    palabras_unicas = set(palabras)
    
    recuento_palabras = {}
    
    for palabra in palabras:
        if palabra in recuento_palabras:
            recuento_palabras[palabra] += 1
        else:
            recuento_palabras[palabra] = 1
            
    print("\n--- Resultados del Análisis ---")
    
    print("Palabras Únicas (Set):")
    print(palabras_unicas)
    
    print("\nRecuento de Palabras (Diccionario):")
    print(recuento_palabras)
    
analizar_frase()

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
#Ejemplo:

def calcular_promedios_alumnos_simple():
    alumnos_notas = {}
    NUM_ALUMNOS = 3
    NUM_NOTAS = 3

    print("--- Carga de Notas ---")
    for i in range(NUM_ALUMNOS):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ").capitalize()
        
        notas_lista = []
        print(f"Ingrese las {NUM_NOTAS} notas para {nombre}:")
        
        for j in range(NUM_NOTAS):
            nota = float(input(f"  Nota {j + 1}: "))
            notas_lista.append(nota)
        
        alumnos_notas[nombre] = tuple(notas_lista)
    
    print("\n--- Resultados de Promedios ---")
    
    for nombre, notas in alumnos_notas.items():
        promedio = sum(notas) / len(notas)
        
        print(f"El promedio de {nombre} es: {promedio:.2f}")

calcular_promedios_alumnos_simple()

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

aprobados_parcial1 = {101, 105, 110, 115, 120, 125}
aprobados_parcial2 = {110, 115, 130, 135, 105, 140}

print("--- Análisis de Aprobados ---")
print(f"P1 Aprobados: {aprobados_parcial1}")
print(f"P2 Aprobados: {aprobados_parcial2}\n")

ambos_parciales = aprobados_parcial1 & aprobados_parcial2
print("1. Estudiantes que aprobaron AMBOS parciales (Intersección):")
print(ambos_parciales)

solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("\n2. Estudiantes que aprobaron SOLO UNO de los dos (Diferencia Simétrica):")
print(solo_uno)

lista_total = aprobados_parcial1 | aprobados_parcial2
print("\n3. Lista TOTAL de estudiantes que aprobaron AL MENOS UN parcial (Unión):")
print(lista_total)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
#Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.

def gestionar_inventario_simple():
    stock = {
        "lapiz": 150,
        "cuaderno": 75,
        "goma": 200,
        "regla": 40
    }

    print("--- Inventario Inicial ---")
    print(stock)
    print("-" * 35)

    producto = input("Ingrese el nombre del producto a gestionar: ").lower()

    if producto in stock:
        stock_actual = stock[producto]
        print(f"\nEl stock actual de '{producto.capitalize()}' es: {stock_actual} unidades.")

        cantidad_a_agregar = int(input("Ingrese la cantidad de unidades que desea añadir (entero, ej. 10): "))
        
        stock[producto] += cantidad_a_agregar
        print(f"Nuevo stock de '{producto.capitalize()}': {stock[producto]}")

    else:
        print(f"\n'{producto.capitalize()}' no se encontró en el inventario.")

        stock_inicial = int(input("Ingrese el stock inicial para el nuevo producto (entero): "))
        
        stock[producto] = stock_inicial
        print(f"Producto '{producto.capitalize()}' agregado con stock: {stock_inicial}")

    print("\n--- Estado Final del Inventario ---")
    print(stock)

gestionar_inventario_simple()

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora

def gestionar_agenda():
    agenda = {
        ("lunes", "10:00"): "Reunión de marketing 'Jugo Vitalia'",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "18:30"): "Entrenamiento de fútbol",
        ("viernes", "09:00"): "Entrega de proyecto final",
        ("viernes", "15:00"): "Cita con el dentista"
    }

    print("--- Consulta de Agenda ---\n")
    
    dia_consulta = input("Ingrese el día que desea consultar (ej: lunes): ").lower()
    hora_consulta = input("Ingrese la hora que desea consultar (formato HH:MM, ej: 10:00): ")
    
    clave_busqueda = (dia_consulta, hora_consulta)
    
    evento = agenda.get(clave_busqueda, "Ninguna actividad programada.")
    
    print("-" * 35)
    print(f"Búsqueda: {dia_consulta.capitalize()} a las {hora_consulta}")
    print(f"Actividad: {evento}")
    print("-" * 35)
gestionar_agenda()

#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

def invertir_diccionario_paises():
    paises_capitales = {
        "argentina": "buenos aires",
        "chile": "santiago",
        "peru": "lima",
        "colombia": "bogota"
    }
    
    capitales_paises = {
        capital: pais 
        for pais, capital in paises_capitales.items()
    }
    
    print("--- Diccionario Original (País: Capital) ---")
    print(paises_capitales)
    
    print("\n--- Diccionario Invertido (Capital: País) ---")
    print(capitales_paises)

invertir_diccionario_paises()

