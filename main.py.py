
accion = 0
actual = 0
while accion != 3:
    print("Menu:")
    print("1. Ingresar nueva compra ")
    print("2. Salir ")
    
    accion = int(input("Seleccione una acción: "))
    if accion == 1:
        nombreCliente=input('Digite su nombre: ')
        while nombreCliente == "":
            nombreCliente= input('El nombre no puede estar vacio, digite nuevamente su nombre: ')
            print('Cambios Jason')
                               
        dia=int(input('Digite el dia: '))
        while dia < 1 or dia > 31:
            dia=int(input("El dia no puede ser menor a 1 o mayor a 31. Digitelo nuevamente. "))

        mes=int(input('Digite el mes: '))
        while mes < 1 or mes > 12:
            mes=int(input("El mes no puede ser menor a 1 o mayor a 12.Digitelo nuevamente. "))

        año=int(input('Digite al año: '))
        while año < 2022:
            año=int(input('El año no puede ser menor al 2022. Digitelo nuevamente '))

        print('La factura de '+nombreCliente+'se genero correctamente el '+str(dia)+'/'+str(mes)+'/'+str(año))

        print("========= LISTA DE PRODUCTOS ========")   
        print("[1]Aceite Soya (1500ml) Precio: 900")
        print('[2]Agua(1,5 litros) Precio: 1200')
        print('[3]Arroz(1kg) Precio:1000')
        print('[4]Atun trocitos(140gr) Precio:1500')


    precio = 0
    bandera=True
    opcion=1
    listaCompra=""

    while bandera:
        cantidad=0
        producto =int(input(' Seleccione un producto digitando el número del mismo '))
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))

        if  producto == 1:
            precioProducto=900* cantidad
            listaCompra+=("Aceite de Soya: "+str(cantidad)+"   "+str(precioProducto)+'\n')
            precio += precioProducto
                    
        elif producto == 2:
           precioProducto=1200 *cantidad
           listaCompra+=("Agua: "+str(cantidad)+"   "+str(precioProducto)+'\n')
           precio += precioProducto


        elif producto == 3:
           precioProducto=1000 *cantidad
           listaCompra+=("Arroz: "+str(cantidad)+"   "+str(precioProducto)+'\n')
           precio += precioProducto
                    
        elif producto ==  4:
            precioProducto=1500 *cantidad
            listaCompra+=("Atun trocitos: "+str(cantidad)+"   "+str(precioProducto)+'\n')
            precio += precioProducto
        else:
            producto=int(print('Producto no existente, porfavor digite un producto existente'))

        respuesta=input('Desea realizar otra compra? |Y| para si o |N| para no ')
        if respuesta == 'N':
            print("============Factura============")
            print(listaCompra)
            print('El precio total es: '+str(precio))
                    
            bandera=False         
    if accion == 2:
        salir= int(input("Saliendo del programa..."))
    else:
        print("Opción inválida. Intente de nuevo.")
