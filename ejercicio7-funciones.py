"""
Hacer un programa que imprima y cuente los múltiplos de 3 que hay entre el 0 y el 20.
"""
"""
inicio = 0
multiplos = 0

while(inicio <= 20):
    if inicio % 3 == 0:
        print(inicio)
        multiplos = multiplos + 1
    inicio = inicio + 1

print("La cantidad de multiplos es de: ",multiplos)
"""


inicio = 0
multiplos = []

def cantidad(listado):
    return len(listado)

while(inicio <= 20):
    if inicio % 3 == 0:
        print(inicio)
        multiplos.append(inicio)
    inicio = inicio + 1

print("Los multiplos son: ",multiplos, "\nLac cantidad de multiplos es de: ", cantidad(multiplos))

#print("Ultimo valor", multiplos[-1])