print("prueba")

accion = 0
actual = 0
while accion != 3:
    print("Menu:")
    print("1. Ingresar nueva compra ")
    print("2. Finalizar compra ")
    print("3. Salir ")
    
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
            print('FECHA INVALIDA , el dia no puede ser mayor a 31 ,  el mes mayor a 12 o el año menor al 2022 ')
            dia=int(input('Digite el dia: '))
            mes=int(input('Digite el mes: '))
            año=int(input('Digite el año: '))
        else:
            print('La factura de '+nombreCliente+'se genero correctamente el '+str(dia)+'/'+str(mes)+'/'+str(año))

        print("=====LISTA DE PRODUCTOS=====")   
        print("[1]Aceite Soya (1500ml) Precio: 900")
        print('[2]Agua(1,5 litros) Precio: 1200')
        print('[3]Arroz(1kg) Precio:1000')
        print('[4] Atun trocitos(140gr) Precio:1000')

        producto =int(input(' Seleccione un producto digitando el número del mismo '))
        if  producto == 1:
            print('Elegiste Aceite de Soya de 1500ml')
            cantidad=int(input('Digite la cantidad de unidades que desea de este producto'))
            precio= 900 * cantidad
        elif producto == 2:
            print('Elegiste Agua de 1.5 litros')
            cantidad=int(input('Digite la cantidad de unidades que desea de este producto'))
            precio= 1200 * cantidad
        elif producto == 3:
            print('Elegiste Arroz de 1kg ')
            cantidad=int(input('Digite la cantidad de unidades que desea de este producto'))
            precio= 1000 * cantidad
        elif producto ==  4:
            print('Elegiste Arroz de 1kg ')
            cantidad=int(input('Digite la cantidad de unidades que desea de este producto'))
            precio= 1000 * cantidad
        else:
                producto=int(print('Producto no existente porfavor digite un producto existente'))

        print(str(precio))
        total= actual+precio    
    elif accion == 2:
         print("El precio a pagar es:", total)   

            
    elif accion == 3:
        salir= int(input("Saliendo del programa..."))
    else:
        print("Opción inválida. Intente de nuevo.")
