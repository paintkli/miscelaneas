"""hacer un programa que nos permita generar la tabla de multiplicar 
de un numero entero positivo iniciando en uno"""

comprobar =True
while comprobar == True:
    n = int(input("ingrese un numero entero positivo:"))
    if n>0:
        for i in range(1,11):
            print (n,"por,i,es iguala:",n*i)
        comprobar = False
    else:
        print("el numero ingresado no es correcto,intente de nuevo")

