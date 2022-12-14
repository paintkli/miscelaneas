""" El usuario es el encargado de suministrar la información de cada persona.
 Vamos a suponer que el usuario solo podrá ingresar un máximo de tres personas"""

 
# Creamos las listas (vacías al comienzo)
nombres = []
identificaciones = []

# Definimos un tamaño para las listas
# Lo puedes cambiar si quieres
tamaño = 3

# Leemos los datos y los agregamos a la lista
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")

    nombres.append(nombre)
    identificaciones.append(identificación)

# Ahora mostremos las listas
for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", nombres[i])
    print("Identificación:", identificaciones[i])