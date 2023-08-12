"""
lista_super = ['frutas', 'verduras', 'lacteos', 'panificados', 'carnes', 
'productos de limpieza', 'embutidos']
"""

"""
lista_super = []
lista_super.append("verduras")
lista_super.append("embutidos")
lista_super.append("lacteos")
"""


import sys
lista_super = []

if(len(sys.argv) == 2):
    lista_super.append(sys.argv(1))
if(len(sys.argv) ==3):
    lista_super.append(sys.argv[1])
    lista_super.append(sys.argv[2])
if(len(sys.argv) == 4):
    lista_super.append(sys.argv[1])
    lista_super.append(sys.argv[2])
    lista_super.append(sys.argv[3])

lista_super.remove("carnes")

print(lista_super, "cantidad:", len(lista_super))
