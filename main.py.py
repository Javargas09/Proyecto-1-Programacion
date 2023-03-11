print("prueba")

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
        mes=int(input('Digite el mes: '))
        año=int(input('Digite al año: '))
        if dia > 31 or mes> 12 or año < 2022:
            print('FECHA INVALIDA , el dia no puede ser mayor a 31 ,  el mes mayor a 12 o el año menor al 2022 ')
            dia=int(input('Digite el dia: '))
            mes=int(input('Digite el mes: '))
            año=int(input('Digite el año: '))
        else:
            print('La factura de '+nombreCliente+'se genero correctamente el '+str(dia)+'/'+str(mes)+'/'+str(año))

        print("========= LISTA DE PRODUCTOS ========")   
        print("[1]Aceite Soya (1500ml) Precio: 900")
        print('[2]Agua(1,5 litros) Precio: 1200')
        print('[3]Arroz(1kg) Precio:1000')
        print('[4]Atun trocitos(140gr) Precio:1000')

        bandera=True
        opcion=1
        precio=0
        cantidad=0

        while bandera:
            if cantidad <= 20:

                producto =int(input(' Seleccione un producto digitando el número del mismo '))

                if  producto == 1:
                    print('Elegiste Aceite de Soya de 1500ml')
                    cantidadProducto=int(input('Digite la cantidad de unidades que desea de este producto'))
                    precio += 900 * cantidad
                    cantidad += cantidadProducto
                    
                elif producto == 2:
                    print('Elegiste Agua de 1.5 litros')
                    cantidadProducto=int(input('Digite la cantidad de unidades que desea de este producto'))
                    precio += 1200 * cantidad
                    cantidad += cantidadProducto

                elif producto == 3:
                    print('Elegiste Arroz de 1kg ')
                    cantidadProducto=int(input('Digite la cantidad de unidades que desea de este producto'))
                    precio += 1000 * cantidad
                    cantidad += cantidadProducto
                    
                elif producto ==  4:
                    print('Elegiste Arroz de 1kg ')
                    cantidadProducto=int(input('Digite la cantidad de unidades que desea de este producto'))
                    precio += 1000 * cantidad
                    cantidad += cantidadProducto
                    
                else:
                    producto=int(print('Producto no existente porfavor digite un producto existente'))

                respuesta=input('Desea realizar otra compra? |Y| para si o |N| para no ')
                if respuesta == 'N':
                    print('El precio total es: '+str(precio))
                    print('La cantidad de productos: '+str(cantidad))
                    
                    bandera=False
            else:
                print("Se excedio la cantidad máxima de productos")      
         
    elif accion == 2:
        salir= int(input("Saliendo del programa..."))
    else:
        print("Opción inválida. Intente de nuevo.")
