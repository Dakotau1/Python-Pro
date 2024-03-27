#Generador de contraseñas
import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

p1 = int(input("Introduzca la longitud deseada de su contraseña: "))
print()

def generador_clave(p1):
    clave = '' #Variable vacía
    for b in range(p1):
        clave += random.choice(caracteres)
    return clave

clave = generador_clave(p1)
print("Contraseña generada:", clave)
