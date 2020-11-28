from datetime import datetime
import random

lista_aleatorios = []
tiempo_1 = 0
tiempo_2 = 0

for i in range(0, 1000):
    lista_aleatorios.append(random.randint(0, 9999))

tiempo_1 = datetime.now()
print(tiempo_1)
#print(lista_aleatorios, "\n")

for i in range(0, len(lista_aleatorios)-1):
    for j in range(0, len(lista_aleatorios)-1):
        if lista_aleatorios[j] > lista_aleatorios[j+1]:
            temporal = lista_aleatorios[j+1]
            lista_aleatorios[j+1] = lista_aleatorios[j]
            lista_aleatorios[j] = temporal

tiempo_2 = datetime.now()
print(tiempo_2)
#print(lista_aleatorios, "\n")

print("El tiempo de ordenamiento es:", tiempo_2 - tiempo_1)
