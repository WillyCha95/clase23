"""
ngresar 5 numeros por teclado y al final de los mismos, el programa debe emitir los siguientes datos: Suma total, Cantidad de numeros impares, y un mensaje que indique si existen números superiores a 100
"""

numeros = []
numero = 1
impares = []
sup_a100 = []


def suma(listado):
    return sum(listado)

def cantidad(lista):
    return len(lista)


while(numero <= 5):
    n = int(input("Ingresa un numero entero: "))
    numeros.append(n)
    if n % 2 != 1:
        impares.append(n)
    if n >= 100:
        sup_a100.append(n)
    numero = numero + 1

"""
print("Numeros en lista:", numeros)
suma = 0
impar = 0
superior_a_100 = 0
posicion = 0

while(len(numeros) > posicion):
    if numeros[posicion] % 2 != 0:
        impar = impar + 1
    if numeros[posicion] >= 100:
        superior_a_100 = superior_a_100 + 1
        posicion = posicion + 1
        """

print("La suma es de: ",suma)
print("La cantidad de numeros impar es de: ",impares)
print("La cantidad superior a 100 es de: ",sup_a100)
