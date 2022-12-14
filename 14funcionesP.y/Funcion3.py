#Escriba una función que pida dos números y que conteste cuál es el menor y cuál el mayor o que escriba que son iguales.

def calcular(n1,n2):
    if n1 > n2:
        print(n1,'es mayor a',n2)
    elif n1 == n2:
        print(n1,'es igual a',n2)
    else:
        print(n1,'es menor a',n2)

num1 = int(input('Digite el primer número'))
num2 = int(input('Digite el segundo número'))

calcular(num1,num2)