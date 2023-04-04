
from clases import nodos
from clases import aristas
from clases import grafo
from random import randint

def Grafo_A(m, directed = False, auto = False):
    
    GRAFO = grafo.Grafo()
    GRAFO.atrbt[grafo.DIRECTED] = directed
    
    for nodo in range(m):
        GRAFO.Producir_Vertices(nodos.Nodo(nodo))
    
    for n1 in range(m):
        for n2 in range(3):
            conexion_aleatoria = randint(0,m-1)
            if n1 != conexion_aleatoria:
                GRAFO.Producir_Aristas(aristas.Arista(n1, conexion_aleatoria),directed,auto)
                #print(f'{n1} -- {conexion_aleatoria}')
            else:
                continue
    
    return GRAFO




 