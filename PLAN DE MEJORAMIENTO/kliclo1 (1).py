## Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

x = input('Digite una palabra: ')

for palabra in range(1,11):
    print(x)

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

## sacar los numeros pares que se encuentran entre 5oo y 1000 y mostrarlos

for i in range(500, 1000, 2):
    print(i)

# crear un ciclo que inicie en 100 y termine en 0

for x in range(100,-1,-1):
    print(x)

#entre el cero y el diez mil muestre  multiplos  de 33 ")

contador = 0 # Iniciamos el contador en cero

for i in range(10000):
    if (i % 33 == 0): # Preguntamos si el residuo es 0 (es múltiplo de 33)
        contador += 1 # Si es múltiplo aumentamos el contad or en 1
    
    # Si no es múltiplo no hacemos nada

#Mostramos el valor del contador
print(contador)

### eddades recorrido por lista

edades = [20, 41, 6, 18, 23]

# Recorriendo los elementos
for edad in edades:
    print(edad)

# Recorriendo los índices
for i in range(len(edades)):
    print(edades[i])

# Con while y los índices
indice = 0

while indice < len(edades):
    print(edades[indice])
    indice += 1
print (edades)    
    ##agregar elementos a una lista append

numeros =[]
numeros.append(8)
numeros.append(12)
numeros.append(34)
print (numeros)

asignaturas=[]
asignaturas.append("ingles")
asignaturas.append("matematica")
asignaturas.append("sociales")
print (asignaturas)

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

asignaturas = ["matemeticas","fisica","quimica","historia","lenguaje"]
print (asignaturas)

#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

    """imprimir los numeros  de 1 a 5 ejecicios de condicionales
cuando x  es menor de 6"""

x = 1
while x < 6:
  print(x)
  x += 1

#Salga del bucle cuando x sea igual a 3:

x = 1
while x < 6:
  print(x)
  if x == 3:
    break
  x += 1
  
  #Imprima un mensaje una vez que la condición sea false:

x = 1
while x < 6:
  print(x)
  x += 1
else:
  print("x no es menor de  6")
## cuanto es el resultado de 39 +50 imprimir felicitaciones repuesta correcta
  
resultado = int(input("¿Cuánto es 39 + 50?"))

if(resultado == 89):
    print("Respuesta Correcta. ¡Felicitaciones!")


## ingrese contraseña correcta e imprimir msn  de bienvenida o incorrecto
##https://www.programarya.com/Cursos/Python/Condicionales/Condicionales-anidados-elif
password = input("Ingrese la contraseña: ")

if(password == "miClave"):
    print("Contraseña correcta. Te damos la bienvenida.")
else:
    print("Contraseña incorrecta.")

## ingresar contraseña leer tamaño de la costarseña  e imprimir si escorrcta  o incorrecta condicional anidado
password = input("Ingrese la contraseña: ")

if (len(password) >= 8):
    print('Tu contraseña es suficientemente larga.')

    if(password == 'miClaveSegura'):
        print("Además es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")
else:
    print('Tu contraseña es muy corta e insegura.')

    if (password != 'miClaveSegura'):
        print("Además, es incorrecta (por supuesto).")

##ahora lo vamos a simplificar con elif
password = input("Ingrese la contraseña: ")

if (len(password) >= 8):
    print('Tu contraseña es suficientemente larga.')

    if(password == 'miClaveSegura'):
        print("Además es la contraseña correcta.")
    else:
        print("Pero es incorrecta.")
elif (password != 'miClaveSegura'):
    print('Tu contraseña es muy corta e insegura.')
    print("Además, es incorrecta (por supuesto).")

    ##diccionarios
    cars= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(cars)