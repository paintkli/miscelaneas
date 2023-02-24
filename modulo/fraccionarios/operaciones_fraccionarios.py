def suma_fra ():
    n1=float(input("ingresa numerador 1 : "))
    d1=float(input("ingresa denominador 1 : "))
    n2=float(input("ingresa numerador 2 : "))
    d2=float(input("ingresa denominador 2 : "))
    if (d1 !=0 and n1!=0):
        print("suma",str(n1/d1+(n2/d2)))
    else:
        print("la divicion entre cero no es posible")


#resta fraccionarios
def resta_fra ():

    n1=float(input("ingresa numerador 1 : "))
    d1=float(input("ingresa denominador 1 : "))
    n2=float(input("ingresa numerador 2 : "))
    d2=float(input("ingresa denominador 2 : "))
    if (d1 !=0 and n1!=0):
        print("resta",str(n1/d1-(n2/d2)))
    else:
        print("la divicion entre cero no es posible")