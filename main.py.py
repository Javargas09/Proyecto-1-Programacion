print("prueba")

accion = 0

while accion != 2:
    print("Menu:")
    print("1. Ingresar nueva compra ")
    print("2. Salir ")
    
    accion = int(input("Seleccione una acción: "))
    if accion == 1:
        #comprar= int(input("Ingresar nueva compra: "))
        nombreCliente=input('Digite su nombre: ')
        while nombreCliente == "":
            nombreCliente= input('El nombre no puede estar vacio, digite nuevamente su nombre: ')
                               
        dia=int(input('Digite el dia: '))
        mes=int(input('Digite el mes: '))
        año=int(input('Digite al año: '))
        if dia > 31 or mes> 12 or año < 2022:
            print('FECHA INVALIDA , el dia no puede ser mayor a 31 ,  el mes mayor a 12 o el año menos al 2022 ')
            dia=int(input('Digite el dia: '))
            mes=int(input('Digite el mes: '))
            año=int(input('Digite al año: '))
        else:
            print('La compra de '+nombreCliente+'se registro correctamente el '+str(dia)+'/'+str(mes)+'/'+str(año))

            
    elif accion == 2:
        salir= int(input("Saliendo del programa..."))
    else:
        print("Opción inválida. Intente de nuevo.")
