print("presiona 0 para salir")
diadesemana= int(input("Introduce un número del 1 al 7: "))

while diadesemana !=0:
    if diadesemana == 1:
        print("Lunes")
    elif diadesemana == 2:
        print("Martes")
    elif diadesemana == 3:
        print("Miércoles")
    elif diadesemana == 4:
        print("Jueves")
    elif diadesemana == 5:
        print("Viernes")
    elif diadesemana == 6:
        print("Sábado")
    elif diadesemana == 7:
        print("Domingo")
    else:
        print("Número no válido")
    diadesemana= int(input("Introduce un número del 1 al 7: "))
