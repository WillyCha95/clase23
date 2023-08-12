"""
Introducir por teclado tantas frases como se deseen y contarlas
"""

contador = 0

while True:
    frase = input("Introduce una frase (o 'salir' para terminar): ")
    
    if frase.lower() == "salir":
        break
    
    contador += 1

print("Total de frases ingresadas:", contador)

#me falta hacer