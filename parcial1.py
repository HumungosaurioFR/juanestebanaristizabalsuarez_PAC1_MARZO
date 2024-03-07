#Crea un programa que solicite al usuario ingresar valores y este debe verificar cuando se ingresa una vocal, el programa debe contar y mostrar la cantidad de vocales (a, e, i, o, u) ingresadas cuantas, de cada una y la cantidad total, importante tener en cuenta que la aplicación se detiene con una opción de menú llamada finalizar. 

import os
os.system('cls')

vocales = 0
contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
while True:
    palabrastr = input('\nBienvenido al sistema de contador de vocales.\n\nPor favor escriba su palabra.\n0. Salir\n\n-> ')
    
    if palabrastr == '0':
        break
    for i in palabrastr:
        if i in 'aeiou':
            vocales += 1
            contador_vocales[i] += 1         
    print(f'\nLa cantidad de vocales es de {vocales}.')        
    print(f'El detalle de las vocales es: {contador_vocales}')
        
        




