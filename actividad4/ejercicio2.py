import datetime as dt
fecha_ingreso=input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
fecha_ingreso=dt.datetime.strptime(fecha_ingreso, "%y-%m-%d")
fecha_actual=dt.datetime.now()

dias= (fecha_actual-fecha_ingreso).days
print(fecha_actual)
print(fecha_ingreso)
print("dias", dias)

if dias >30:
    print("cuenta inactiva")