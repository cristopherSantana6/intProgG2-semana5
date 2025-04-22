#Ingresar la cantidad inicial en inventario
#Ingresar la cantidad de productos recibidos
#Ingresar la cantidad de productos vendidos
#Sumar los productos recibidos al inventario inicial
#Restar los productos vendidos del total anterior
#Guardar el resultado como inventario actual
#Mostrar el inventario inicial
#Mostrar los productos recibidos y vendidos
#Mostrar el inventario final disponible
inventario=int(input("Ingrese el inventario inicial: "))
recibidos=int(input("Ingrese la cantidad de productos recibidos: "))
vendidos=int(input("Ingrese la cantidad de productos vendidos: "))
suma=inventario+recibidos
resta=suma-vendidos
inventario_actual=resta
print(f"""Inventario inicial: {inventario:>3}
Productos recibidos: {recibidos:>2}
Productos vendidos: {vendidos:>3}
{"Inventario actual: ":<15} {inventario_actual:>3}""")