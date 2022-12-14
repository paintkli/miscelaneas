#Crear una funcion que convierta grados kelvin a celsius.

def convertir(k):
    celsius = k - 272.15
    return celsius

kelvin = int(input('Grados a convertir: '))

print(convertir(kelvin))