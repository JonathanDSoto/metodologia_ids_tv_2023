sueldo = 0

print("Ingrese el sueldo: ")
sueldo = input()

sueldo = float(sueldo)

if(sueldo < 5000 ):
    print("Aplic aumento del 15% ")
    print("Bono de: ", sueldo * 0.15)
    print("Total; ", sueldo + sueldo * 0.15)
else:
    print("Aplic aumento del 12% ")
    print("Bono de: ", sueldo * 0.12)
    print("Total; ", sueldo + sueldo * 0.12)