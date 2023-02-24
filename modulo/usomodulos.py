from sys import path

path.append('..\\modulo')
import funciones
import fraccionarios.operaciones_fraccionarios
print(funciones.sumar(1,1))
fraccionarios.operaciones_fraccionarios.suma_fra()

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)