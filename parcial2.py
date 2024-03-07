import os
os.system('cls')

numeroint = int(input("Ingresa un número entero positivo: "))
if numeroint > 0:
    for i in range(1, 11):
        print(f"{numeroint} x {i} = {numeroint*i}")
else:
    print("El número debe ser positivo")
