#len = longitud, while = mientras

import sys

def obtener_alumnos(posicion, listad):
    posicion = int(posicion)
    return "El alumno en posicion: "+ str (posicion) + "es" + listado[posicion]

listado_de_alumnos = []

posicion = 0

while((len(sys.argv) -1) != len(listado_de_alumnos)):
    listado_de_alumnos.append(sys.argv[posicion])
    posicion = posicion + 1

listado_de_alumnos.remove("union.py")

lugar = input("Introduce la posicion del alumno a mostrar: ")
print(obtener_alumnos(lugar, listado_de_alumnos))
#print("Listados de alumnos,", listado_de_alumnos)
#print("Alumno en la posicion 4", listado_de_alumnos[4])

