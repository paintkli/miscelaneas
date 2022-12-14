#Escriba una función que avise cuando se escriben valores negativos o nulos.

def negativo (n):
    if n < 0:
        print("este numero es negativo")
    else:
        print("este numero es positivo")

numero = float(input('Digite un número'))

negativo(numero)
