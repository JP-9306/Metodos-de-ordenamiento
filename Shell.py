from datetime import datetime
import random


def ordenamientoDeShell(unaLista):
    contadorSublistas = len(unaLista)//2
    while contadorSublistas > 0:

        for posicionInicio in range(contadorSublistas):
            brechaOrdenamientoPorInsercion(
                unaLista, posicionInicio, contadorSublistas)

        contadorSublistas = contadorSublistas // 2


def brechaOrdenamientoPorInsercion(unaLista, inicio, brecha):
    for i in range(inicio+brecha, len(unaLista), brecha):

        valorActual = unaLista[i]
        posicion = i

        while posicion >= brecha and unaLista[posicion-brecha] > valorActual:
            unaLista[posicion] = unaLista[posicion-brecha]
            posicion = posicion-brecha

        unaLista[posicion] = valorActual


lista_aleatorios = []
tiempo_1 = 0
tiempo_2 = 0

for i in range(0, 1000):
    lista_aleatorios.append(random.randint(0, 9999))

tiempo_1 = datetime.now()
print(tiempo_1)
#print(lista_aleatorios, "\n")

ordenamientoDeShell(lista_aleatorios)

tiempo_2 = datetime.now()
print(tiempo_2)
#print(lista_aleatorios, "\n")

print("El tiempo de ordenamiento es:", tiempo_2 - tiempo_1)
