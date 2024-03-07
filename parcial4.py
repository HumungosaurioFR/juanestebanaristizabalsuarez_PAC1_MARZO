import os
os.system('cls')

opcionstr = int(input('Ingresa la categoría del producto:\n\n1. Ferreteria\n2. Aseo\n3. Seguridad\n4. Alimentos\n5. Electrodomesticos\n\n->  '))
precioflt = float(input('Ingresa el precio del producto: '))
if opcionstr == 1:
    discount = 0.10
elif opcionstr == 2:
    discount = 0.05
elif opcionstr == 3:
    discount = 0.15
elif opcionstr == 4:
    discount = 0.08
elif opcionstr == 5:
    discount = 0.12
else:
    print('Categoría inválida')
    exit()

final_price = precioflt - (precioflt * discount)

print('\nPrecio final:', final_price)
print('Descuento:', discount)
print('Categoría:', opcionstr)