from clases import nodos
from clases import aristas
from clases import grafo
from random import randint

"""
La funcion Dorogo_M crear un triangulo de 3 nodos unido cons determinados aristas
y el usuario de los n nodos que ingreso se va ir acumulando las aristas una por una hasta termina con los nodos

"""
def Dorogo_M(n, directed=False):    
    GRAFO = grafo.Grafo()
    GRAFO.atrbt[grafo.DIRECTED] = directed

    # Se crea un Triangulo de nodos 
    for nodo in range(3): # creamos 3 nodos
        GRAFO.Producir_Vertices(nodos.Nodo(nodo))
    #De los nodos creados se unen las aristas para formar el triangulo    
    for arista in range(3):  # creamos 3 aristas 
        union = arista + 1 if arista < 2 else 0
        GRAFO.Producir_Aristas(aristas.Arista(arista, union), directed)
     
    # Una vez formado el triangulo los nodos se unen a los extremos del grafo de forma aleatoria
    for nodo in range(3, n):
        GRAFO.Producir_Vertices(nodos.Nodo(nodo)) # se genera el nodo        
        union = randint(0, len(GRAFO.Aristas_Aleatorias()) - 1) # Selecciona al azar una arista del grafo
        arista = GRAFO.Aristas_Aleatorias()[union] #se genera la conexion al grafp
        (a1, a2) = arista # Arista finalizada
        GRAFO.Producir_Aristas(aristas.Arista(nodo, a1), directed) # Se conecta la arista al nodo 
        GRAFO.Producir_Aristas(aristas.Arista(nodo, a2), directed) # Se conecta la arista al nodo

    return GRAFO

