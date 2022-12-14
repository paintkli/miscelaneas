#Escriba un programa que permita crear una lista de palabras. Para ello, 
#el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. 
#Por último, el programa tiene que escribir la lista.

numero = int(input("Cuántas palabras tiene la lista: "))

lista = []

if numero < 1:
      print("Debe ingresar un número mayor a 0")
else:
    for i in range(numero):
        palabra = input("Digite una palabra: ")
        lista += [palabra]
    print("La lista con las palabras es: ",lista)

#https://www.mclibre.org/consultar/python/ejercicios/ej-listas-1.html