#ejercicio 1
multiplos_de_4 = []

for numero in range(1, 101):
    if numero % 4 == 0:
        multiplos_de_4.append(numero)
        
print(multiplos_de_4)

#ejercicio 2
# Crear una lista con cinco elementos que te gusten
colores = ["rojo", "azul", "verde", "amarillo", "blanco"]

penultimo_elemento = colores[-2]

print(f"La lista completa es: {colores}")
print(f"El penúltimo elemento de la lista es: {penultimo_elemento}")

#ejercicio 3
mi_lista = []

mi_lista.append("manzana")
mi_lista.append("banana")
mi_lista.append("cereza")

print(mi_lista)

#ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#ejercicio 5
#El programa realiza lo siguiente:
#Define una lista de números que contiene los valores [8, 15, 3, 22, 7].
#Busca el número más grande: La función max(numeros) se ejecuta para encontrar el valor más grande dentro de la lista numeros. En este caso, el valor más alto es 22.
#Elimina ese número: El método .remove() se utiliza para eliminar la primera aparición del valor que se le pasa como argumento. Como el argumento es max(numeros), el programa elimina el número 22 de la lista.
#Imprime la lista modificada: Finalmente, la función print(numeros) muestra el contenido de la lista después de que se ha eliminado el número 22.
#La lista original [8, 15, 3, 22, 7] se convierte en [8, 15, 3, 7] y ese es el resultado que se imprime en pantalla.

#ejercicio 6
numeros = list(range(10, 31, 5))

print(numeros[0:2])

#ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["SUV", "camioneta"]
print(autos)

#ejercicio 8
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

#ejercicio 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)