#Ingresar la distancia recorrida en kilómetros
#Ingresar la cantidad de litros consumidos
#Dividir la distancia entre los litros
#Guardar el resultado como rendimiento (km/l)
#Multiplicar los litros por el precio por litro (definirlo)
#Guardar el resultado como gasto total en combustible
#Mostrar la distancia, litros y precio por litro
#Mostrar el rendimiento del vehículo
#Mostrar el gasto total en combustible

distancia=float(input("Ingrese la distancia recorrida (km): "))
litros=float(input("Ingrese la cantidad de litros consumidos: "))
precio_por_litro=48.97
rendimiento=distancia/litros
gasto_total=litros*precio_por_litro
print(f"""Distancia recorrida: {distancia:>3} km
Litros consumidos: {litros:>3} l
Precio por litro: {precio_por_litro:>3} $
{"Rendimiento del vehículo: ":<15} {rendimiento:>3.0f} km/l
{"Gasto total en combustible: ":<15} {gasto_total:>3.2f} $""")