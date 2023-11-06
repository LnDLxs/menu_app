# Función para agregar una compra
def agregar_compra(compra, monto):
    compras.append((compra, monto))
    print("Compra agregada correctamente.")

# Función para mostrar las compras
def mostrar_compras():
    if len(compras) == 0:
        print("No hay compras registradas.")
    else:
        for i, compra in enumerate(compras):
            print(f"{i +1}. {compra[0]} - {compra[1]} €")

# Función para mostrar el total gastado
def mostrar_total():
    print(f"Total gastado: {total_gastado:2f} €")

# Función principal
def main():
    global compras
    global total_gastado

    compras = []
    total_gastado = 0

    while True:
        #imprimir el menú
        print("** Menu **")
        print("1. Agregar compra")
        print("2. Mostrar compra")
        print("3. Mostrar total gastado")
        print("4. Salir")

        # Solicita una opcion al usuario
        opcion = input("Selecione una opcion:  ")

        # Verifica la opción selecionada
        if opcion == "1":
            # Solicita el nombre del producto
            producto = input("Ingrese el nombre de la compra:  ")

            # Solicita el monto de la compra
            monto = float(input("Ingrese el monto de la compra:  "))

            # Agrega la compra a la lista
            agregar_compra(producto, monto)

            # Actualiza el total gastado
            total_gastado += monto

        elif opcion == "2":
            mostrar_compras()

        elif opcion == "3":
            mostrar_total()

        elif opcion == "4":
            print("!Hasta Luego¡")
            break

        else:
            print("Opción invalida.")

# Llama a la función principal
if __name__ == "__main__":
    main()
