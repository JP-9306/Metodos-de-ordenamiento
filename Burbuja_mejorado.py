from datetime import datetime
import random

lista_aleatorios = []
tiempo_1 = 0
tiempo_2 = 0
bandera = False

for i in range(0, 1000):
    lista_aleatorios.append(random.randint(0, 9999))

longitud_arreglo = len(lista_aleatorios)
comparaciones = longitud_arreglo

tiempo_1 = datetime.now()
print(tiempo_1)
#print(lista_aleatorios, "\n")

for i in range(0, longitud_arreglo-1):
    if (bandera):
        break
    bandera = True
    for j in range(0, comparaciones-1):
        if lista_aleatorios[j] > lista_aleatorios[j+1]:
            temporal = lista_aleatorios[j+1]
            lista_aleatorios[j+1] = lista_aleatorios[j]
            lista_aleatorios[j] = temporal
            bandera = False        
    comparaciones -= 1

tiempo_2 = datetime.now()
print(tiempo_2)
#print(lista_aleatorios, "\n")

print("El tiempo de ordenamiento es:", tiempo_2 - tiempo_1)
