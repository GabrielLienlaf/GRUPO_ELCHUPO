#crear un menu de concierto de opera Donde:
#compramos 1
#Debe permitir mostar bombre del comprador y seleccionar un show por separada
#para que la compra sea exitosa debemos cumplir los siguientes:
#A) nombre del comprador ni debe repetirse
#b)la seleccion del show debe permitir seleccionar entradas para
#  una de las 2 funciones.
    #funcion 1 : el lago de cisne
    # funcion 2: stock de las funciones
#cambiamos sow 2
# mostar stock de las funciones 3



def comprar_entradas(stock,compradores):
    print("compra de entradas")
    nombre = input("Ingrese nombre del comprador: ")

    if nombre in compradores:
        print("Erro: EL NOMBRE YA EXISTE")
        return stock
    
    print("Seleccione una funcion:")
    print("1) funcion es el lado de cisce y hay 50 entradas disponibles")
    print("2) funcion  Tributo y hay 60 entradas disponibles")
    opcion = int(input("Seleccione una Funcion: "))
    if opcion not in (1, 2):
        print("Error opcion invalida")
        return stock
    if opcion == 1:
        if stock ["f1"] <= 0:
            print("Error: Sin stock disponible para la funcion 1")
            return stock
        stock["f1"] -= 1
    else:
        if stock["f2"] <= 0:
            print("Error: sin stock disponible para la funcion 2")
            return stock
        stock["f2"] -= 1




    compradores[nombre] = opcion
    print (f"Entrada  registrada en la funcion {opcion}! stock restante: Funcion 1: {stock["f1"]}  \n"f"funcion1 {stock["f1"]} \n funcion2 : {stock["f2"]}")




    #def mostrar_stock

    #def cambiar_funcion


def main():
    stock = {"f1":10, "f2" : 5 }
    compradores = {}
    while True:
        print("1) Comprar entradas")
        print("")
        print("")
        print("")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            stock = comprar_entradas(stock,compradores)
        elif opcion == 2:
            print("")
        elif opcion == 3:
            print("")
        elif opcion == 4:
            print("")

if __name__ == "__main__":
        main()