def es_triangulo(lado1, lado2, lado3):
    suma= lado1+lado2
    if (suma > lado3):
        return "Es un triángulo"
    else:
        return "No es un triángulo"
def main():
    print("ingrese los siguientes valores") 
    print("="*20)
    lado1= float(input("lado1: "))
    lado2= float(input("lado2: "))
    lado3= float(input("lado3: "))
    print(es_triangulo(lado1, lado2, lado3))

main()