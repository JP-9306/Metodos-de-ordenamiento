# Autor: JP-9306
# Comparativo de tiempos de ordenamiento por distintos métodos

from datetime import datetime
import random

# METODO DE ORDENAMIENTO BURBUJA


def burbuja(lista):
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-1):
            # Intercambia los valores si el valor actual es mayor que el siguiente
            if lista[j] > lista[j+1]:
                temporal = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = temporal

    tiempo = datetime.now()

    return tiempo


# METODO BURBUJA MEJORADO O CON BANDERA
def burbuja_mejorado(lista):
    # Esta será la bandera con la que indicaremos hasta que punto del arreglo ya se encuentra ordenado
    # para no volver a tratar de ordenarlo como sucede en el metodo burbuja convencional
    bandera = False

    longitud_arreglo = len(lista)  # Obtiene el tamaño de la lista
    comparaciones = longitud_arreglo
    for i in range(0, longitud_arreglo-1):
        if (bandera):
            # Si la bandera es positiva, entonces deja de evaluar y salta al siguiente elemento
            break
        bandera = True
        for j in range(0, comparaciones-1):
            if lista[j] > lista[j+1]:
                # Intercambia los valores si el valor actual es mayor que el siguiente
                temporal = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = temporal
                bandera = False
        comparaciones -= 1  # Disminuye el número de comparaciones a realizar

    tiempo = datetime.now()

    return tiempo


# METODO DE ORDENAMIENTO POR INSERCION
def insercion(lista):
    longitud_arreglo = len(lista)  # Obtiene el tamaño del arreglo
    for i in range(1, longitud_arreglo):
        # 'pivote' será el valor con el que compararemos a los valores anteriores
        pivote = lista[i]
        j = i-1

        while (j >= 0 and lista[j] > pivote):
            # Evaluaremos los valores entre el valor inicial y el pivote
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = pivote

    tiempo = datetime.now()

    return tiempo


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


def shell(lista):
    ordenamientoDeShell(lista)
    tiempo = datetime.now()

    return tiempo


def main():
    # Creación de la lista donde alojaremos los valores aleatorios
    lista_aleatorios = []

    for i in range(0, 100000):
        # Se agregan valores aleatorios a la lista
        lista_aleatorios.append(random.randint(0, 9999))

    # Se ejecuta la función del metodo burbuja y se obtiene su hora y fecha inicial y final
    print("\nMETODO BURBUJA")
    inicio_burbuja = datetime.now()
    print("Tiempo inicial:", inicio_burbuja)
    tiempo_burbuja = burbuja(lista_aleatorios)
    print("Tiempo final:", tiempo_burbuja)

    # Se ejecuta la función del metodo burbuja mejorado y se obtiene su hora y fecha inicial y final
    print("\nMETODO BURBUJA MEJORADO")
    inicio_burbuja_mejorado = datetime.now()
    print("Tiempo inicial:", inicio_burbuja_mejorado)
    tiempo_burbuja_mejorado = burbuja_mejorado(lista_aleatorios)
    print("Tiempo final:", tiempo_burbuja_mejorado)

    # Se ejecuta la función del metodo por inserción y se obtiene su hora y fecha inicial y final
    print("\nMETODO POR INSERCIÓN")
    inicio_insercion = datetime.now()
    print("Tiempo inicial:", inicio_insercion)
    tiempo_insercion = insercion(lista_aleatorios)
    print("Tiempo final:", tiempo_insercion)

    # Se ejecuta la función del metodo shell y se obtiene su hora y fecha inicial y final
    print("\nMETODO SHELL")
    inicio_shell = datetime.now()
    print("Tiempo inicial:", inicio_shell)
    tiempo_shell = shell(lista_aleatorios)
    print("Tiempo final:", tiempo_shell)

    # Se presentan los tiempos que tardó cada uno de los métodos
    print("\n\nTIEMPOS DE ORDENAMIENTO\n")
    print("Método burbuja:\t\t\t\t", tiempo_burbuja - inicio_burbuja)
    print("Método burbuja mejorado:\t\t",
          tiempo_burbuja_mejorado - inicio_burbuja_mejorado)
    print("Método inserción:\t\t\t", tiempo_insercion - inicio_insercion)
    print("Método Shell:\t\t\t\t", tiempo_shell - inicio_shell)


main()
