import os

# Crear un diccionario para almacenar el inventario
inventario = {}

# Función para agregar un nuevo producto al inventario
def agregar_producto():
    os.system('cls||clear') 
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad disponible: "))
    precio = float(input("Ingrese el precio unitario: "))
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print("Producto agregado con éxito.")

# Función para eliminar un producto del inventario
def eliminar_producto():
    os.system('cls||clear') 
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado con éxito.")
    else:
        print("El producto no existe en el inventario.")

# Función para mostrar el inventario completo
def mostrar_inventario():
    os.system('cls||clear')  # Limpiar pantalla
    print("Inventario:")
    for nombre, info in inventario.items():
        print(nombre + ": cantidad=" + str(info["cantidad"]) + ", precio=" + str(info["precio"]))

# Función para buscar un producto en el inventario
def buscar_producto():
    os.system('cls||clear') 
    nombre = input("Ingrese el nombre del producto a buscar: ")
    if nombre in inventario:
        print(nombre + ": cantidad=" + str(inventario[nombre]["cantidad"]) + ", precio=" + str(inventario[nombre]["precio"]))
    else:
        print("El producto no existe en el inventario.")

# Menú principal del programa
while True:
    print("\nSeleccione una opción:")
    print("1. Agregar un nuevo producto")
    print("2. Eliminar un producto existente")
    print("3. Mostrar el inventario completo")
    print("4. Buscar un producto")
    print("5. Salir del programa")
    opcion = int(input("Opción seleccionada: "))
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        eliminar_producto()
    elif opcion == 3:
        mostrar_inventario()
    elif opcion == 4:
        buscar_producto()
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Intente de nuevo.")
