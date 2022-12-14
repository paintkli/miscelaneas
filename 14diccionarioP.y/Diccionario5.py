#Cree un diccionario vacío y llenelo con los equiposque considere
#que van a pasar  a cuartos de final del mundial

dicc = {'estudiantes':{}} 

while True:

    nombre = input('Ingrese el nombre del estudiante: ')
    if nombre == '':
        break
    aprobar = input("Escriba 'aprueba' o 'reprueba' según su consideración: ")

    dicc['estudiantes'][nombre] = aprobar

    print(dicc)