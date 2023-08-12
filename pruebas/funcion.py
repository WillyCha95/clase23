"""
def = (definir) nombre_funcion():
    print("Hola desde la funcion")

nombre_funcion()
"""

import sys
import os

def saludar(nombre, test = os.getlogin()):
    if(nombre == ''):
        nombre='Asistente'
    print("Hola, me llamo", nombre,"y vos? Seguro te llamas", test)

nombre = input("Ingresa un nombre para el asitente: ")

try:
    saludar(nombre, sys.argv[1])
except:
    saludar(nombre)
