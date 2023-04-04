
from clases import nodos
from clases import aristas
from clases import grafo

"""
Funcion Malla, Que Genera un grafo tipo Malla de n*m nodos, que ingresa el usuario
"""

def Malla(m, n, directed=False):
    GRAFO = grafo.Grafo()
    GRAFO.atrbt[grafo.DIRECTED] = directed
    flag = []
    for i in range(1,m):
        i = i*m
        flag.append(i)
    #Variable que multiplica las varibles m y n para calcular los nodos totales
    nodos_totales = m*n
    # Crea una interacion de 0 a nodo_totales para crear los nodos 
    for nodo in range(nodos_totales):
        GRAFO.Producir_Vertices(nodos.Nodo(nodo))
    # Crea una iteracion  sobre otra iteracion donde los nodos totales genera aristas de conexion para formar una malla
    for a in range(nodos_totales):
        for b in range(nodos_totales):
            if a != b:
                if (b-a) == 1:
                    if b in flag:
                        continue
                    else:
                        #Crea una arista entre b y a si su diferencia es 1
                        GRAFO.Producir_Aristas(aristas.Arista(a,b),directed)
                elif (b-a) == m:
                    #Crea una arista entre b y a si su diferencia es igual a m
                    GRAFO.Producir_Aristas(aristas.Arista(a,b),directed)
            else:
                continue
    return GRAFO

