

# Variables globales
codigo = 1
listado_productos = []

def registrar_producto():
    global codigo
    try:
        descripcion = input("Ingrese descripción: ").strip()
        precio = float(input("Ingrese precio: "))
        cantidad = int(input("Ingrese cantidad: "))
        
        producto = {
            "codigo": codigo,
            "descripcion": descripcion,
            "precio": precio,
            "cantidad": cantidad
        }
        listado_productos.append(producto)
        codigo += 1
        print("Producto registrado con éxito.\n")
    except ValueError:
        print("Error: Ingrese datos numéricos válidos para precio y cantidad.\n")

def buscar_producto_por_codigo():
    try:
        cod_buscar = int(input("Ingrese el código del producto a buscar: "))
        for p in listado_productos:
            if p["codigo"] == cod_buscar:
                print("Producto encontrado:")
                print(f"Código: {p['codigo']}")
                print(f"Descripción: {p['descripcion']}")
                print(f"Precio: {p['precio']}")
                print(f"Cantidad: {p['cantidad']}\n")
                return
        print("Producto no encontrado.\n")
    except ValueError:
        print("Error: Ingrese un código válido.\n")

def imprimir_productos():
    if not listado_productos:
        print("No hay productos registrados.\n")
        return
    for p in listado_productos:
        print(f"Código: {p['codigo']}")
        print(f"Descripción: {p['descripcion']}")
        print(f"Precio: {p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        print("-" * 20)
    print()

def editar_producto():
    cod_editar = int(input("Ingrese el código del producto a editar: "))
    estado = True
    
    for p in listado_productos:
        if p["codigo"] == cod_editar:

            while estado:

                print("Que decea cambiar? ")
                print("1) Descripción")
                print("2) Precio")
                print("3) cantidad")
                print("4) Salir")
                op = input("Escoja una opcion: ")

                

                if op == "1": 
                        
                    nueva_desc = input(f"Descripción actual: {p['descripcion']} -> ")
                    p['descripcion'] = nueva_desc
                    

                elif op == "2":
                    nueva_precio = input(f"Precio actual: {p['precio']} -> ")
                    p['Precio'] = nueva_precio
                    

                elif op == "3":
                    nueva_cantidad = input(f"Cantidad actual: {p['cantidad']} -> ")
                    p['cantidad'] = nueva_cantidad
                    

                elif op == "4":
                    estado = False

                print("Producto actualizado con éxito.\n")   

def eliminar_producto():
    try:
        cod_eliminar = int(input("Ingrese el código del producto a eliminar: "))
        for i, p in enumerate(listado_productos):
            if p['codigo'] == cod_eliminar:
                del listado_productos[i]
                print("Producto eliminado correctamente.\n")
                return
        print("Producto no encontrado.\n")
    except ValueError:
        print("Código inválido.\n")

def menu():
    while True:
        print('--- MENÚ DE PRODUCTOS ---')
        print('1 - Registrar producto')
        print('2 - Buscar producto por código')
        print('3 - Imprimir productos')
        print('4 - Editar producto')
        print('5 - Eliminar producto por código')
        print('6 - Salir')
        try:
            opcion = int(input('Ingrese una opción: '))
        except ValueError:
            print("Por favor ingrese un número válido.\n")
            continue

        if opcion == 1:
            registrar_producto()
        elif opcion == 2:
            buscar_producto_por_codigo()
        elif opcion == 3:
            imprimir_productos()
        elif opcion == 4:
            editar_producto()
        elif opcion == 5:
            eliminar_producto()
        elif opcion == 6:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

menu()