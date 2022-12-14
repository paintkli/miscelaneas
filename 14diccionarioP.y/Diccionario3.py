#Escribe un programa python que pida un número por teclado y que cree un diccionario 
#cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

numero = int(input("Ingrese un número: "))

dicc = {}

for num in range(1,numero+1):
    dicc[num] = num ** 2

print(dicc)

#https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u32/