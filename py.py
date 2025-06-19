lista = []
codigo = 1

while True:
    print("++++ Menu ++++")
    print("1) Registrar producto")
    print("2) Buscar producto por código")
    print("3) Imprimir productos")
    print("4) Editar producto (Descripción | Precio | Cantidad)")
    print("5) Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        descripcion = input("Ingrese descripción: ")
        precio = float(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad: "))

        producto = {
            "codigo": codigo,
            "descripcion": descripcion,
            "precio": precio,
            "cantidad": cantidad
        }
        lista.append(producto)
        codigo += 1
        print("Producto registrado con exito.")

    elif opcion == "2":
        buscar = int(input("¿que codigo quieres buscar?: "))
        encontrado = False
        for x in producto.values():
          print(x)

    elif opcion == "3":
        print("\n--- Lista de productos ---")
        for p in lista:
            print(p)

    elif opcion == "4":
        cod = int(input("Ingrese código del producto a editar: "))
        for p in lista:
            if p["codigo"] == cod:
                print(f"Editando producto: {p}")
                print("1) Editar descripción")
                print("2) Editar precio")
                print("3) Editar cantidad")
                edit_opcion = input("Seleccione una opción: ")
                
                if edit_opcion == "1":
                    nueva_descripcion = input("Nueva descripción: ")
                    p["descripcion"] = nueva_descripcion
                elif edit_opcion == "2":
                    nuevo_precio = float(input("Nuevo precio: "))
                    p["precio"] = nuevo_precio
                elif edit_opcion == "3":
                    nueva_cantidad = int(input("Nueva cantidad: "))
                    p["cantidad"] = nueva_cantidad
                
    elif opcion == "5":
        print("Saliendo del programa.")
        break