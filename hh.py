




codi = 0
cambiar = 0
producto_cambiar = ""
lista = []
opcion = ""
contador = 0
contador_dicc = 0
while True:
    print("***Menu***")
    print("1) Agregar Poducto")
    print("2)Buscar producto")
    print("3)Imprimir todos los productos ")
    print("4)Editar producto(Descripción/Precio/Cantidad)")
    print("5)Eliminar producto por codigo")
    opcion = input("elija una opcion: ")


    if opcion == "1":
       
        contador +=1
        producto = input("Que producto desea llevar: ")
        precio = str(input("Precio del Producto: "))
        cantidad = str(input("Igrese cantidad: "))

        dicc = {
        "codigo" : contador,
        "descipción" : producto,
        "precio" : precio,
        "cantidad" : cantidad
        }
        lista.append(dicc)
        for x, y in dicc.items():
            print(x, y)

    elif opcion == "2":
        busqueda = int(input("Ingrese el codigo de lo que desea buscar :"))
        co = busqueda - 1
        for a in lista[co].items():
            print(a)

    elif opcion == "3":

        for a in lista:

            print(a)


    elif opcion == "4":

        while True:

            print("1)Editar Producto")  
            print("2)Editar Precio")
            print("3)Editar Cantidad")

            op = input("Escoja una opción: ")

            if op == "1":

                cambiar = int(input("Escoja el producto que quiere cambiar: "))

                codi = cambiar - 

                producto_cambiar = input("Ingrese producto")

                producto_cambiar =  lista[codi][producto]

                print(lista[codi])

                