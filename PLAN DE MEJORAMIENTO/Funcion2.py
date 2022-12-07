#Escribir una función que muestre por pantalla el saludo Hola y el nombre del usuario.

def saludo(n):
    return 'hola', n #Si hay un return dentro de la función, se invoca con un print por fuera.

nombre = input('Digite su nombre: ')

print(saludo(nombre))