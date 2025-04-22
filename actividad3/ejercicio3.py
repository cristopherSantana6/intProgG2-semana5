#Ingresar el capital inicial
#Ingresar la tasa de interés anual (en porcentaje)
#Ingresar la cantidad de años
#Convertir la tasa porcentual a decimal
#Calcular el valor de (1 + tasa)^años
#Guardar el resultado como monto final
#Restar el capital inicial del monto final para obtener el interés ganado
#Mostrar el capital inicial, la tasa y los años
#Mostrar el monto final y el interés ganado

capital_inicial=float(input("Ingrese el capital inicial: "))
tasa=float(input("Ingrese la tasa de interés anual (en porcentaje): ").replace("%", ""))
años=int(input("Ingrese la cantidad de años: "))
tasa_decimal=tasa/100
monto_final=capital_inicial*(1+tasa_decimal)**años
interes_ganado=monto_final-capital_inicial
print(f"""Capital inicial: {capital_inicial:>18.2f}
Tasa de interés anual: {tasa:>10.2f} % 
Cantidad de años: {años:>17}
{"Monto final: ":<15} {monto_final:>19.2f}
{"Interés ganado: ":<15} {interes_ganado:>18.2f}""")