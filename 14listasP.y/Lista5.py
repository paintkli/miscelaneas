#Escriba un programa que permita crear una lista de palabras y que, a continuación, 
#pida una palabra y diga cuántas veces aparece esa palabra en la lista.
  
numero = int(input("Cuántas palabras tiene la lista: "))

lista = []

if numero < 1:
      print("Debe ingresar un número mayor a 0")
else:
    for i in range(numero):
        palabra = input("Digite una palabra: ")
        lista += [palabra]
    print("La lista con las palabras es: ",lista)

buscar = input("Dígame la palabra a buscar: ")

contador = 0

for palabra in lista:
    if palabra == buscar:
        contador += 1
if contador == 0:
    print("La palabra ",buscar," no aparece en la lista.")
elif contador == 1:
    print("La palabra ",buscar," aparece una vez en la lista.")
else:
    print("La palabra ",buscar," aparece ",contador," veces en la lista.")