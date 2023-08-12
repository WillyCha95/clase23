"""
Hacer un programa que imprima todos los numeros
enteros que hay desde la unidad hasta un número que introduciremos por teclado.
"""

hasta = int(input("Introduce el valor maximo: "))
numeros = []

def cantidad(lista):
    return len(lista)

while(cantidad(numeros) < hasta):
    numeros.append(cantidad(numeros) + 1)

print(numeros)