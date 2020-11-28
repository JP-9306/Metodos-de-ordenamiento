from datetime import datetime
import random

lista_aleatorios = []
tiempo_1 = 0
tiempo_2 = 0

for i in range(0, 1000):
    lista_aleatorios.append(random.randint(0, 9999))

longitud_arreglo = len(lista_aleatorios)

tiempo_1 = datetime.now()
print(tiempo_1)
#print(lista_aleatorios, "\n")

for i in range(1, longitud_arreglo):
    pivote = lista_aleatorios[i]
    j = i-1

    while (j >= 0 and lista_aleatorios[j] > pivote):
        lista_aleatorios[j+1] = lista_aleatorios[j]
        j -= 1
    lista_aleatorios[j+1] = pivote
    
tiempo_2 = datetime.now()
print(tiempo_2)
#print(lista_aleatorios, "\n")

print("El tiempo de ordenamiento es:", tiempo_2 - tiempo_1)
