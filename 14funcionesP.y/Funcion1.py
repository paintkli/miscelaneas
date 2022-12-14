# Escribir una función que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def mostrarEdad(n):#se coloca def para definir una función, luego el nombre y los paréntesis. Dentro de los 
                    #paréntesis va el parámetro.

    if n < 18: #if es una condición
        print ("Eres menor de edad.")
    else:#elif es de lo contrario si:
        print("Eres mayor de edad.")

edad = int(input("¿Cuál es tu edad? "))#int --> número / input --> texto

mostrarEdad(edad)