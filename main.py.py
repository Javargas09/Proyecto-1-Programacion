accion = 0
actual = 0
def descuento(cantidad, precio):
    precioIva = precio * 0.13

    if cantidad <= 5:
        precioDescuento = precio - (precio * 0.02)
    elif cantidad > 5 and cantidad <= 10:
        precioDescuento = precio - (precio * 0.05)
    elif cantidad > 10:
        precioDescuento = precio - (precio * 0.07)

    precioNeto = precioDescuento + precioIva

    print('El precio total con descuento es: ' + str(precioDescuento))
    print('El precio neto es: ' + str(precioNeto))

while accion != 2:
    print("Menu:")
    print("1. Ingresar nueva compra ")
    print("2. Salir ")
    
    accion = int(input("Seleccione una acción: "))
    if accion == 1:
        nombreCliente=input('Digite su nombre: ')
        while nombreCliente == "":
            nombreCliente= input('El nombre no puede estar vacio, digite nuevamente su nombre: ')
                               
        dia=int(input('Digite el dia(Entre el 1 y el 31): '))
        while dia < 1 or dia > 31:
            dia=int(input("El dia no puede ser menor a 1 o mayor a 31. Digitelo nuevamente. "))

        mes=int(input('Digite el mes(Entre el el mes 1 y el 12): '))
        while mes < 1 or mes > 12:
            mes=int(input("El mes no puede ser menor a 1 o mayor a 12.Digitelo nuevamente. "))
            
        año=int(input('Digite al año(Del 2022 en adelante): '))
        while año < 2022:
            año=int(input('El año no puede ser menor al 2022. Digitelo nuevamente '))

        print('La factura de '+nombreCliente+' se genero correctamente el '+str(dia)+'/'+str(mes)+'/'+str(año))

        print("========= LISTA DE PRODUCTOS ========")   
        print("[1]Aceite Soya (1500ml) Precio: 900")
        print('[2]Agua(1,5 litros) Precio: 1,200')
        print('[3]Arroz(1kg) Precio:1,000')
        print('[4]Atun trocitos(140gr) Precio:1500')
        print('[5]Salmón(1kg) Precio:11,495')
        print('[6]Lomo ancho sin hueso(1kg) Precio:8,095')
        print('[7]Lomo Delmonico(1kg) Precio:8,225')
        print('[8]Bistec de Res(1kg) Precio:5,675')
        print('[9]Lengua de Res(1kg) Precio:8,425')
        print('[10]Punta de Solomo(1kg) Precio:7,825')
        print('[11]Carne Molida (88-12)(1kg) Precio:3,950')
        print('[12]Mano de Piedra(1kg) Precio:7,350')
        print('[13]Chuleta de Cerdo(1kg) Precio:3,195')
        print('[14]Lomo de Cerdo(1kg) Precio:5,425')
        print('[15]Bistec de Cerdo(1kg) Precio:3,975')
        print('[16]Pechuga de Pollo(1kg) Precio:3,050')
        print('[17]Muslito sin piel(1kg) Precio:3,575')
        print('[18]Muslo de Pollo(1kg) Precio:1,895')
        print('[19]Filete de Tilapia(1kg) Precio:6,525')
        print('[20]Deditos de Pescado(273gr) Precio:6,895')
        print('[21]Filete de Corvina(800gr) Precio:11,695')
        print('[22]Filete de Tilapia Empanizado(1kg) Precio:6,175')
        print('[23]Huevos (60 unidades) Precio:7,898')
        print('[24]Eggo waffles chocochips(2,1kg) Precio:12,995')
        print('[25]Eggo waffles(1.4kg) Precio:6,955')
        print('[26]Mrs.Butterworth Jarabe Orginal(1.9L) Precio:3,895')
        print('[27]Azúcar(6kg) Precio:3,975')
        print('[28]Endulzante con Estevia(500unidades) Precio:5,495')
        print('[29]Papas Sazonadas con Cáscara(2kg) Precio:4,895')
        print('[30]Papas a la Francesa(2.5kg) Precio:3,395')
        
        



        precio = 0
        cantidadTotal=0
        bandera=True
        opcion=1
        listaCompra=""
    
        contador=1
        #CAMBIAR UN 4 POR EL 20. EL 4 ES SOLO PARA PROBAR
        while bandera and contador <= 4:
            cantidad=0
            producto =int(input(' Seleccione un producto digitando el número del mismo '))
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))

            if  producto == 1:
                precioProducto=900* cantidad
                listaCompra+=("Aceite de Soya: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad
                        
            elif producto == 2:
                precioProducto=1200 *cantidad
                listaCompra+=("Agua: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad


            elif producto == 3:
                precioProducto=1000 *cantidad
                listaCompra+=("Arroz: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad  

            elif producto ==  4:
                precioProducto=1500 *cantidad
                listaCompra+=("Atun trocitos: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  5:
                precioProducto=11495 *cantidad
                listaCompra+=("Salmón: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  6:
                precioProducto=8095 *cantidad
                listaCompra+=("Lomo ancho sin hueso: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  7:
                precioProducto=8225 *cantidad
                listaCompra+=("Lomo Delmonico: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  8:
                precioProducto=5675 *cantidad
                listaCompra+=("Bistec de Res: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  9:
                precioProducto=8425 *cantidad
                listaCompra+=("Lengua de Res: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  10:
                precioProducto=7825 *cantidad
                listaCompra+=("Punta de Solomo: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  11:
                precioProducto=3950 *cantidad
                listaCompra+=("Carne Molida: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  12:
                precioProducto=7350 *cantidad
                listaCompra+=("Mano de Piedra: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  13:
                precioProducto=3195 *cantidad
                listaCompra+=("Chuleta de Cerdo: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  14:
                precioProducto=5425 *cantidad
                listaCompra+=("Lomo de Cerdo: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  15:
                precioProducto=3975 *cantidad
                listaCompra+=("Bistec de Cerdo: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad
        
            elif producto ==  16:
                precioProducto=3050 *cantidad
                listaCompra+=("Pechuga de Pollo: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  17:
                precioProducto=3575 *cantidad
                listaCompra+=("Muslito sin piel: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  18:
                precioProducto=1895 *cantidad
                listaCompra+=("Muslo de Pollo: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  19:
                precioProducto=6525 *cantidad
                listaCompra+=("Filete de Tilapia: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  20:
                precioProducto=6895 *cantidad
                listaCompra+=("Deditos de Pescado: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  21:
                precioProducto=11695 *cantidad
                listaCompra+=("Filete de Corvina: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  22:
                precioProducto=6175 *cantidad
                listaCompra+=("Filete de Tilapia Empanizado: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  23:
                precioProducto=7898 *cantidad
                listaCompra+=("Huevos: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  24:
                precioProducto=12995 *cantidad
                listaCompra+=("Eggo waffles chocochips: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  25:
                precioProducto=6955 *cantidad
                listaCompra+=("Eggo waffles: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad
        
            elif producto ==  26:
                precioProducto=3895 *cantidad
                listaCompra+=("Mrs.Butterworth Jarabe Orginal: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  27:
                precioProducto=3975 *cantidad
                listaCompra+=("Azúcar: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  28:
                precioProducto=5495 *cantidad
                listaCompra+=("Endulzante con Estevia: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  29:
                precioProducto=4895 *cantidad
                listaCompra+=("Papas Sazonadas con Cáscara: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad

            elif producto ==  30:
                precioProducto=3395 *cantidad
                listaCompra+=("Papas a la Francesa: "+str(cantidad)+"   "+str(precioProducto)+'\n')
                precio += precioProducto
                cantidadTotal += cantidad
            else:
                producto=int(print('Producto no existente, porfavor digite un producto existente'))

            contador += 1
            if contador <= 4:
                respuesta=input('Desea realizar otra compra? |Y| para si o |N| para no ')
                #CAMBIAR EL 5 POR UN 21. 5 SOLO PARA PROBAR
                if respuesta == 'N' or contador == 5:
                    print("============Factura============")
                    print(listaCompra)
                    print('El precio total es: ' + str(precio))       
                    #print("La cantidad total de productos es: "+str(cantidadTotal)) 
                    descuento(cantidadTotal, precio)
                    
                    bandera=False
            else:
                print("Ha alcanzado el limite de 20 productos en la factura.Realice una nueva compra")
                print(listaCompra)
                print("El precio total es: " + str(precio))
                descuento(cantidadTotal, precio)
                #print("La cantidad total de productos es: "+str(cantidadTotal))

                bandera=False        
    if accion == 2:
        salir= int(input("Saliendo del programa..."))
