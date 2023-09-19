sueldo = 0

print("Ingrese el sueldo: ")
sueldo = input()

sueldo = float(sueldo)

if( sueldo < 3000 ):
    print("Aplica un aumento")
    print("Aumento: ",sueldo * 0.15)
    print("Total: ",sueldo + (sueldo*0.15))
else:
    print("No aplica aumento")