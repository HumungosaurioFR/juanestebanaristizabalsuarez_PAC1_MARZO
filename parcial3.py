import os
os.system('cls')
while True:
    opcionstr = input('Por favor selecciona una unidad\n\nc. Centigrados\nf. Fahrenheit\nX. Salir\n\n-> ')

    if opcionstr == 'c' or opcionstr == 'C':
        gradosFflt = float(input('\nIngrese la cantidad de grados Fahrenheit -> '))
        gradoscflt = (gradosFflt - 32) * 5/9
        print(f'\nLos grados centigrados son:{gradoscflt}\n')
    
    if opcionstr == 'f' or opcionstr == 'F':
        gradoscfloat = float(input('\nIngrese la cantidad de grados Celsius -> '))
        gradosfflta = (gradoscfloat * 9/5) + 32
        print(f'\nLa conversion a Fahrenheit es:{gradosfflta} \n')
        
    if opcionstr == 'x' or opcionstr == 'X':
        print("\n¡Hasta luego!")
        break

