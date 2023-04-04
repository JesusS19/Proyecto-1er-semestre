from clases import nodos
from clases import aristas
from clases import grafo
from random import random


def Barabasi(n, d, directed=False, auto=False):
    GRAFO= grafo.Grafo()
    GRAFO.atrbt[grafo.DIRECTED] = directed

    #Se crean 10 vertices en este caso elegi 10 pero el usuario puede modificarlo, 
    for nodo in range(10):
        GRAFO.Producir_Vertices(nodos.Nodo(nodo))
    # Se crean d aristas que se conectan entre todos los vertices creados
    for i in range(d):
        for j in range(d):
            if len(GRAFO.Trayectoria_Normal(i)) < d and len(GRAFO.Trayectoria_Normal(j)) < d:
                GRAFO.Producir_Aristas(aristas.Arista(i, j), directed, auto)
    #CRea los nodos y las aristas restantes.
    for i in range(10, n):
        GRAFO.Producir_Vertices(nodos.Nodo(i))
        for j in range(i):
            probabilidad = len(GRAFO.Trayectoria_Normal(j)) / len(GRAFO.Aristas_Aleatorias())
            if len(GRAFO.Trayectoria_Normal(i)) < d and len(GRAFO.Trayectoria_Normal(j)) < d and probabilidad >= random():
                GRAFO.Producir_Aristas(aristas.Arista(i, j), directed, auto)
    return GRAFO