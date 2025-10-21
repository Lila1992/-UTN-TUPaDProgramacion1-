#1. Crear archivo inicial con productos: Crear un archivo de texto llamado
#productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

nombre_archivo = "productos.txt"

productos_con_salto = [
    "celular,1200.50,15\n",
    "mouse Inalámbrico,25.99,50\n",
    "monitor 27 Pulgadas,350.00,20\n"
]

with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    archivo.writelines(productos_con_salto)
    
print(f"Archivo '{nombre_archivo}' creado.")

print("\nContenido del archivo:")
with open(nombre_archivo, 'r', encoding='utf-8') as archivo_verificacion:
    print(archivo_verificacion.read().strip())

#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
#línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
#formato:
#Producto: Lapicera | Precio: $120.5 | Cantidad: 30

nombre_archivo = "productos.txt"

print(f"Leyendo y mostrando productos desde '{nombre_archivo}':\n")

with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre, precio_str, cantidad_str = datos
        
        precio = float(precio_str)
        cantidad = int(cantidad_str)
        
        print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")


#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
#cantidad) y lo agregue al archivo sin borrar el contenido existente

nombre_archivo = "productos.txt"

print(f"PRODUCTOS ACTUALES EN '{nombre_archivo}' ---")
with open(nombre_archivo, 'r', encoding='utf-8') as archivo_lectura:
    for linea in archivo_lectura:
        datos = linea.strip().split(",")
        nombre, precio_str, cantidad_str = datos
        precio = float(precio_str)
        cantidad = int(cantidad_str)
        print(f"Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad}")


print("Ingrese los datos del nuevo producto:")
nuevo_nombre = input("Nombre: ")
nuevo_precio = input("Precio: ")
nueva_cantidad = input("Cantidad: ")

nueva_linea = f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n"

print(f"\n Agregando '{nuevo_nombre}' al archivo...")
with open(nombre_archivo, 'a', encoding='utf-8') as archivo_escritura:
    archivo_escritura.write(nueva_linea)

print("Producto agregado")

print("\n CONTENIDO FINAL DEL ARCHIVO ---")
with open(nombre_archivo, 'r', encoding='utf-8') as archivo_verificacion:
    print(archivo_verificacion.read().strip())


#4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
#una lista llamada productos, donde cada elemento sea un diccionario con claves:
#nombre, precio, cantidad.

nombre_archivo = "productos.txt"
productos = []

print(f"cargando datos desde '{nombre_archivo}' en la lista de diccionarios 'productos'...")

with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre_str, precio_str, cantidad_str = datos
        
        precio = float(precio_str)
        cantidad = int(cantidad_str)
        
        producto_dict = {
            'nombre': nombre_str,
            'precio': precio,
            'cantidad': cantidad
        }
        
        productos.append(producto_dict)

print("carga completa.\n")

print("contenido final de la lista 'productos':")
for producto in productos:
    print(producto)


#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
#producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
#no existe, mostrar un mensaje de error

nombre_archivo = "productos.txt"
productos = [] 
with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        datos = linea.strip().split(",")
        nombre_str, precio_str, cantidad_str = datos
        productos.append({
            'nombre': nombre_str,
            'precio': float(precio_str),
            'cantidad': int(cantidad_str)
        })

print("\n BUSCADOR DE PRODUCTOS ---")

nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ").strip()
producto_encontrado = None

for producto in productos:
    if producto['nombre'].lower() == nombre_buscado.lower():
        producto_encontrado = producto
        break 
        

if producto_encontrado:
    print(f"Producto '{nombre_buscado}' encontrado! Detalles:")
    print(f"  Nombre: {producto_encontrado['nombre']}")
    print(f"  Precio: ${producto_encontrado['precio']:.2f}")
    print(f"  Cantidad en stock: {producto_encontrado['cantidad']}")
else:
    print(f"error: El producto '{nombre_buscado}' no se encuentra en el inventario.")


#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
#productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
#productos actualizados desde la lista.

productos = [
    {'nombre': 'Laptop', 'precio': 1200.5, 'cantidad': 15},
    {'nombre': 'Mouse Inalámbrico', 'precio': 25.99, 'cantidad': 50},
    {'nombre': 'Monitor 27 Pulgadas', 'precio': 350.0, 'cantidad': 20},
    {'nombre': 'Teclado Mecánico', 'precio': 75.0, 'cantidad': 35} 
]

nombre_archivo = "productos.txt"

print(f"Sobrescribiendo el archivo '{nombre_archivo}' con {len(productos)} productos actualizados...")

with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        
        archivo.write(linea)
        
print("Archivo guardado con éxito. La información ha sido actualizada persistentemente.\n")

print("Contenido final de productos.txt:")
with open(nombre_archivo, 'r', encoding='utf-8') as archivo_verificacion:
    print(archivo_verificacion.read().strip())