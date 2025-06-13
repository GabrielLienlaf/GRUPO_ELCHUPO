
comida = 0
while comida != 4:
    print("****Menu Principal - Comida Rapida****")
    print("1) Hamburgesas")
    print("2) Pizzas")
    print("3) Bebidas")
    print("4) Salir y Mostar total")
    try:
        op = int(input("Seleccione una opcion (1-4): "))
    except ValueError as uno:
        print(f"Error {uno} Debe ingresar un numero valido")

    if op == 1:
        ch_1 = 8
        tc = 12
        ops = 0
        while ops != 3 :
            
            print("***Hamburgesas***")
            print("1) Chedar - $8")
            print("2) tocino - $12")
            print("3) volver al menu principal")

            try:
                ops = int(input("seleccione una hamburgesa (1-3): "))

            except ValueError as uno:

                print(f"Error {uno} Debe ingresar un numero valido")
            if ops == 1:
                 
                 try:
                    cant_1 = int(input("¿Cuantas de chedar llevaras?: "))

                 except ValueError as dos:
                     
                     print(f"Error {dos} Debe ingresar un numero valido")

                 ch_1 = ch_1 * cant_1
                 print(f"Chedar: {cant_1} =${ch_1} ")

            if ops == 2:
                 
                 try:
                    cant_2 = int(input("¿Cuantas de tocino llevaras?: "))

                 except ValueError as dos_1:
                     
                     print(f"Error {dos_1} Debe ingresar un numero valido")

                 tc = tc * cant_2
                 print(f"Chedar: {cant_2} =${tc} ")
    if op == 2:
        n = 20
        p = 15
        ops1 = 0
        while ops1 != 3 :
            
            print("***Pizzas***")
            print("1) napolitana - $20")
            print("2) peperoni - $15")
            print("3) volver al menu principal")

            try:
                ops1 = int(input("seleccione una Pizza (1-3): "))

            except ValueError as p_2:

                print(f"Error {p_2} Debe ingresar un numero valido")
            if ops1 == 1:
                 
                 try:
                    cant_3 = int(input("¿Cuantas de napolitanas llevaras?: "))

                 except ValueError as p_3:
                     
                     print(f"Error {p_3} Debe ingresar un numero valido")

                 n = n * cant_3
                 print(f"napolitana: {cant_3} =${n} ")

            if ops1 == 2:
                 
                 try:
                    cant_4 = int(input("¿Cuantas de peperoni llevaras?: "))

                 except ValueError as p_2:
                     
                     print(f"Error {p_2} Debe ingresar un numero valido")

                 p = p * cant_4
                 print(f"Chedar: {cant_4} =${p} ")
    if op == 3:
        c = 2
        ps = 1
        ops3 = 0
        while ops3 != 3 :
            
            print("***bebidas***")
            print("1) cocacola - $2")
            print("2) pepsi - $1")
            print("3) volver al menu principal")

            try:
                ops3 = int(input("seleccione una opcion (1-3): "))

            except ValueError as b_3:

                print(f"Error {b_3} Debe ingresar un numero valido")
            if ops3 == 1:
                 
                 try:
                    cants_1 = int(input("¿Cuantas de Cocacolas llevaras?: "))

                 except ValueError as b_1:
                     
                     print(f"Error {b_1} Debe ingresar un numero valido")

                 c = c * cants_1
                 print(f"Cocacola: {cants_1} =${c} ")

            if ops3 == 2:
                 
                 try:
                    cants_2 = int(input("¿Cuantas de Pepsips llevaras?: "))

                 except ValueError as b_2:
                     
                     print(f"Error {b_2} Debe ingresar un numero valido")

                 ps = ps * cants_2
                 print(f"pepsips: {cants_2} =${ps} ")    

    if op == 4:
        total = tc + ch_1 + p + n + c + ps
        print(f"Total a pagar: ${total}")