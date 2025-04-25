sueldo=float(input("Ingrese su sueldo: "))
bono =0
if sueldo >3000:
    bono = sueldo * 0.1
elif sueldo >1500 and sueldo <=3000:
    bono = sueldo * 0.05
elif sueldo <=1500:
    print("No tiene bono") 
print(f"su sueldo es:  {sueldo:.2f}")
print(f"su bono es: {bono:.2f}")    
print(f"su sueldo total es: {sueldo + bono: .2f}")