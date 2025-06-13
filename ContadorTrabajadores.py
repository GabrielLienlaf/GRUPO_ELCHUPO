# Contadores

mayores_10 = 0

menores_o_iguales_10 = 0



# Solicita cantidad de empleados con validación

while True:

  try:

    cantidad = int(input("Ingrese la cantidad de empleados a registrar: "))

    if cantidad < 1:

      print("Debe ingresar un número entero positivo.")

      continue

    break

  except ValueError:

    print("Debe ingresar un número entero.")



# Registrar cada empleado

for i in range(cantidad):

  nombre = input("Ingrese nombre del empleado: ")



  while True:

    try:

      anos = int(input("Ingrese años de antigüedad: "))

      break

    except ValueError:

      print("Debe ingresar un número entero.")



  if anos > 10:

    print("Más de 10 años de antigüedad.")

    mayores_10 += 1

  else:

    print("10 o menos años de antigüedad.")

    menores_o_iguales_10 += 1



# Resultado final

print(f"\nSe registraron {mayores_10} empleados con más de 10 años de antigüedad.")

print(f"Se registraron {menores_o_iguales_10} empleados con 10 o menos años de antigüedad.")

