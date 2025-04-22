#Ingresar el total de litros consumidos en un mes en una vivienda
#Ingresar la cantidad de personas que viven en la casa
#Dividir los litros totales entre la cantidad de personas
#Guardar el resultado como consumo mensual por persona
#Dividir el consumo mensual por 30 para obtener el consumo diario
#Guardar ese resultado como consumo diario por persona
#Mostrar el consumo total del mes
#Mostrar la cantidad de personas en la vivienda
#Mostrar el consumo mensual y diario por persona

consumo=float(input("Ingrese el total de litros consumidos en un mes: "))
personas=int(input("Ingrese la cantidad de personas que viven en la casa: "))
consumo_mensual_por_persona=consumo/personas
consumo_diario_por_persona=consumo_mensual_por_persona/30
print(f"""Consumo total del mes: {consumo:>3} litros
Cantidad de personas en la vivienda: {personas:>3}
Consumo mensual por persona: {consumo_mensual_por_persona:>3.2f} litros
Consumo diario por persona: {consumo_diario_por_persona:>3.2f} litros""")