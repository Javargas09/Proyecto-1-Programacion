print("prueba")

accion = 0

while accion != 2:
    print("Menu:")
    print("1. Ingresar nueva compra ")
    print("2. Salir ")
    
    accion = int(input("Seleccione una acción: "))

    if accion == 1:
        comprar= int(input("Ingresar nueva compra: "))
    elif accion == 2:
        salir= int(input("Saliendo del programa..."))
    else:
        print("Opción inválida. Intente de nuevo.")