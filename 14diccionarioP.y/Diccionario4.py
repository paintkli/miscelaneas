"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
 pregunte al usuario por una fruta, un número de kilos y muestre por pantalla 
 el precio de ese número de kilos de fruta. Si la fruta no está 
 en el diccionario debe mostrar un mensaje informando de ello.
Fruta	       Precio
Plátano	       1.350
Manzana	       5.800
Pera	       3.850
Naranja	       2.700"""


frutas = {'Platano':1.350, 'Manzana':5.800, 'Pera':3.850, 'Naranja':2.700,}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")