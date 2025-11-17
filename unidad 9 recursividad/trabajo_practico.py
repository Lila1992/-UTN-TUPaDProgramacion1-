#1)Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
#función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def calcular_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

def main():
    print(" Calculadora de Factoriales Recursivos")
    numero_limite = 5
    print(f"Usaremos el número límite: {numero_limite}")

    print("\nResultados:")
    # iteramos desde 1 hasta el número limite
    for i in range(1, numero_limite + 1):
        # Llamamos a funcion
        resultado = calcular_factorial(i)
        print(f"El factorial de {i}! es: {resultado}")

if __name__ == "__main__":
    main()

#2)Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique

def fibonacci(n):
    # Caso Base 1: Posicion 0 es 0.
    if n == 0:
        return 0
    # Caso Base 2: Posicion 1 es 1.
    elif n == 1:
        return 1
    # Caso Recursivo: El valor es la suma de los dos valores anteriores.
    else:
        # La recursion se detiene en los casos base 0 y 1.
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print("Calculadora de la Serie de Fibonacci")
    # Definimos un límite fijo para simplificar el código (Posiciones 0 a 8).
    posicion_limite = 8
    print(f"Calculando la serie hasta la posición: {posicion_limite}")
    serie = []
    # Iteramos desde la posicion 0 hasta la posición lim.
    for i in range(posicion_limite + 1):
        # Llamamos a la funcion recursiva para obtener el valor.
        valor_fib = fibonacci(i)
        serie.append(str(valor_fib))
    
    # Mostramos la serie completa en una sola linea.
    print("\nSerie de Fibonacci completa:")
    print(", ".join(serie))

if __name__ == "__main__":
    main()

#3)Crea una función recursiva que calcule la potencia de un número base elevado a un
#exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1)
#Prueba esta función en un algoritmo general.

def calcular_potencia(base, exponente):
    # Caso Base 1
    if exponente == 0:
        return 1
    # Caso Base 2
    if exponente == 1:
        return base
    # Caso Recursivo
    else:
        return base * calcular_potencia(base, exponente - 1)

def main():
    print("Calculadora de Potencia Recursiva")
    print("Fórmula utilizada: n^m = n * n^(m-1)")
    BASE = 4
    EXPONENTE = 3
    print(f"\nCalculando: {BASE} elevado a la {EXPONENTE} ({BASE}^{EXPONENTE})")
    # Llamamos a la funcion recusiva
    resultado = calcular_potencia(BASE, EXPONENTE)
    print(f"El resultado recursivo de {BASE}^{EXPONENTE} es: {resultado}")
    print("Comprobación (4 * 4 * 4): 64")

if __name__ == "__main__":
    main()

#4)Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# Ejemplo:
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".

def decimal_a_binario(n):
    # Caso Base
    if n == 0:
        return ""
    # Paso Recursivo: Calcula el cociente y el resto (0 o 1).
    cociente = n // 2
    resto = n % 2
    # Primero la llamada recursiva (para invertir el orden)
    # y luego se concatena el digito actual (el resto).
    return decimal_a_binario(cociente) + str(resto)

def main():
    print("Conversor Decimal a Binario Recursivo")
    # Definimos un numero 
    NUMERO_A_CONVERTIR = 13 # El binario esperado es 1101
    if NUMERO_A_CONVERTIR == 0:
        resultado = "0"
    else:
        # Llamamos a la funcion recursiva
        resultado = decimal_a_binario(NUMERO_A_CONVERTIR)
    # Mostramos el resultado
    print(f"\nEl numero decimal {NUMERO_A_CONVERTIR} se convierte en binario como: {resultado}")
    print("-----------------------------------------------------")
    print("¡Funcion recursiva completada!")
# Ejecutamos el programa principal
if __name__ == "__main__":
    main()

#5)Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    """
    Función recursiva que verifica si una cadena de texto es un palindromo.
    Se compara el primer carácter con el último en cada llamada.
    """
    # 1. Caso Base: 
    if len(palabra) <= 1:
        return True
    # 2. Caso Recursivo:
    # Si los extremos son diferentes, retorna False inmediatamente.
    if palabra[0] != palabra[-1]:
        return False
    # Si son iguales, se llama recursivamente a la porcion interna.
    else:
        return es_palindromo(palabra[1:-1])

#Programa Principal
def main():
    print("Verificador de Palindromos Recursivo")
    # Ejemplo 1: Palindromo
    palabra_palindromo = "anilina"
    es_1 = es_palindromo(palabra_palindromo)
    print(f"\nLa palabra '{palabra_palindromo}' es palindromo: {es_1}") # Esperado: True
    # Ejemplo 2: No Palíndromo
    palabra_no_palindromo = "ejemplo"
    es_2 = es_palindromo(palabra_no_palindromo)
    print(f"La palabra '{palabra_no_palindromo}' es palindromo: {es_2}") # Esperado: False
# ejecutamos programa principal
if __name__ == "__main__":
    main()

#6)Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
#suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    """calcula la suma de todos los digitos de un numero entero positivo 'n'
    utilizando operaciones matematicas y recursividad.
    """
    # 1. Caso Base
    if n == 0:
        return 0
    # 2. Caso Recursivo:
    ultimo_digito = n % 10
    # n // 10: Reduce el numero quitando el ultimo digito (division entera).
    numero_reducido = n // 10
    # Retorno: Suma el ultimo digito con la suma recursiva del numero reducido.
    return ultimo_digito + suma_digitos(numero_reducido)
# Programa Principal
def main():
    print("Suma de Dígitos Recursiva")
    # Definimos un unico numero de prueba
    NUMERO_DE_PRUEBA = 789
    # Llamamos a la función recursiva
    resultado = suma_digitos(NUMERO_DE_PRUEBA)
    # Mostramos el resultado (7 + 8 + 9 = 24)
    print(f"\nEl número de prueba es: {NUMERO_DE_PRUEBA}")
    print(f"La suma de sus dígitos es: {resultado}")
    print("------------------------------------------")
# Ejecutamos el programa principal
if __name__ == "__main__":
    main()

#7)Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    """funcion recursiva que calcula el total de bloques necesarios para construir
    una piramide, sumando desde 'n' hasta 1.
    """
    # 1. Caso Base:
    if n <= 1:
        return n 
    # 2. Paso Recursivo:
    return n + contar_bloques(n - 1)
#programa Principal
def main():
    print("Contador de Bloques de Piramide Recursivo")
    # definimos un unico ejemplo fijo para la demostracion
    NIVEL_BASE = 4
    print(f"Calculando el total de bloques si la base tiene {NIVEL_BASE} bloques (4 + 3 + 2 + 1):")
    # llamamos a la funcion recursiva
    resultado = contar_bloques(NIVEL_BASE)
    # mostramos el resultado
    print(f"\nEl total de bloques necesarios es: {resultado}")
    print("-----------------------------------------------------")
# ejecutamos el programa principal
if __name__ == "__main__":
    main()

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 
# contar_digito(123456, 7) → 0 

def contar_digito(numero, digito):
    """funcion recursiva que cuenta cuantas veces aparece un 'digito' especifico
    dentro de un 'numero' entero positivo.
    """
    # 1. Caso Base:
    # La recursion se detiene cuando el numero a analizar es 0.
    if numero == 0:
        return 0
    # 2. Paso Recursivo:
    # extraer el ultimo dígito
    ultimo_digito = numero % 10
    contador_actual = 1 if ultimo_digito == digito else 0
    # reducir el numero quitando el ultimo digito
    numero_reducido = numero // 10
    # Retorno: Suma el contador actual mas el resultado recursivo del subproblema.
    return contador_actual + contar_digito(numero_reducido, digito)
#programa Principal
def main():
    print("Contador de Digitos Recursivo")
    # Definimos un unico ejemplo fijo para la demostración
    NUMERO_DE_PRUEBA = 12233421
    DIGITO_A_BUSCAR = 2 # El resultado esperado es 3
    # llamamos a la función recursiva
    resultado = contar_digito(NUMERO_DE_PRUEBA, DIGITO_A_BUSCAR)
    # Mostramos el resultado
    print(f"\nNúmero: {NUMERO_DE_PRUEBA}, Digito a contar: {DIGITO_A_BUSCAR}")
    print(f"El dígito aparece: {resultado} veces.")
    print("------------------------------------------")
# ejecutamos el programa principal
if __name__ == "__main__":
    main()
    