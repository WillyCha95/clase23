"""
Hacer un programa que imprima los numeros impares entre el 10 y el cero en orden decreciente
calcule la suma de esos numeros impares
"""

suma_impares = 0

for i in range(10, -1, -1):
    if i % 2 != 0:  
        print(i)
        suma_impares += i

print("La suma de los números impares es:", suma_impares)
