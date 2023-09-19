#encontrar el mayor de 3 num 

num1 = input("Ingrese el num1: ")
num2 = int(input("Ingrese el num2: "))
num3 = float(input("Ingrese el num3: "))

num1 = int(num1)

if( num1 > num2 ):
    if(num1 > num3):
        print(num1)

if(num2 > num1 and num2 > num3):
    print(num2)

if(num3 > num1 and num3 > num2):
    print(num3)
