calificacion= float(input("Ingrese su calificacion: "))
if calificacion >= 9 and calificacion <= 10:
    print("A")
elif calificacion >= 7 and calificacion <= 8:
    print("B")
elif calificacion >= 5 and calificacion <= 6:
    print("C")
elif calificacion >= 3 and calificacion <= 4:
    print("D")
elif calificacion >= 0 and calificacion <= 2:
    print("F")
else:
    print("Calificacion no valida")