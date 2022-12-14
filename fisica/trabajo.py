"""
Una persona mueve una caja con una cuerda a una distancia horizontal de 15 m.
Esta cuerda forma un ángulo de 30° con respecto a la horizontal del piso. 
Si la tensión que presenta la cuerda es de 6N. ¿Cuál es el trabajo realizado?-
"""
import os, time, math

def trabajo (dist, angu):
    radian=(angu*math.pi)/180
    traba=6*(dist*math.cos(radian))
    return traba

def datos ():
    while True:
        try:
            print ("Una persona mueve una caja con una cuerda a una distancia horizontal de: ", end="")
            distancia=int(input())
            print ("Esta cuerda forma un ángulo de: ", end="")
            angulo=int(input())
            print("con respecto a la horizontal del piso.")
            print("Si la tensión que presenta la cuerda es de 6N. ¿Cuál es el trabajo realizado?")
            break
        except ValueError:        
            print ("Upss !! no fue un número valido, intente de nuevo")
        except:
            print ("Upss !! tipo de error desconocido, vuelva a intentar")
    return (trabajo(distancia,angulo))


print("Una persona mueve una caja con una cuerda a una distancia horizontal de 15 m.")
print("Esta cuerda forma un ángulo de 30° con respecto a la horizontal del piso")
print("Si la tensión que presenta la cuerda es de 6N. ¿Cuál es el trabajo realizado?-")
dat=datos()
print ("-"*80)
print ("     El trabajo realizado es de:  ",dat," J")
print ("-"*80)
