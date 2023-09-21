monto = float(input("monto: "))

if (monto < 500):
    print("No hay descuento")
    
elif(monto >= 500 and monto <1000):
    print("Descuento del 5% ")
    desc = monto * 0.05
    print("total: ",monto - desc)
    
elif(monto >= 1000 and monto <7000):
    print("Descuento del 11% ")
    desc = monto * 0.11
    print("total: ",monto - desc)
    
elif(monto >= 7000 and monto <15000):
    print("Descuento del 18% ")
    desc = monto * 0.18
    print("total: ",monto - desc)
    
elif(monto >= 15000):
    print("Descuento del 25% ")
    desc = monto * 0.25
    print("total: ",monto - desc)