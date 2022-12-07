## solo cuando el número ingresado sea igual a 0 se detiene,
#  así que la condición para que se siga ejecutando es que el numero NO sea 0.


numero = float(input('Ingresa un número. 0 para terminar: '))

while(numero != 0):
    numero = float(input('Ingresa un número. 0 para terminar: '))

print('Fin del programa.')

## otra forma de hacerlo


while(True):
    numero = float(input('Ingresa un número. 0 para terminar: '))

    if (numero == 0):
        break

print('Fin del programa.')