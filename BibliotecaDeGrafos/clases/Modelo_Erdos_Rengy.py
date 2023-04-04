from clases import nodos
from clases import aristas
from clases import grafo
from random import randint

"""
Funcion Erdos_Reyi, crear un grafo donde el usuario ingresa n nodos y m aristas, el grafo creara
m aristas hasta que termine de crear las aristas ingresada por el usuario, sin embargo las aristas
se crearan de forma aleatoria entre o y n nodos ingresados 
"""
def Erdos_Renyi(n, m, directed = False, auto = False):
    flag_arista = {}
    GRAFO = grafo.Grafo()
    GRAFO.atrbt[grafo.DIRECTED] = directed
    # Iteracion que produce n vertices.
    for nodo in range(n):
        GRAFO.Producir_Vertices(nodos.Nodo(nodo))

    i=1
    #Mientras i sea menor o igual a m, se generan aristas sin que estas se hayan repetido o
    #los valores de las aristas elegidas al azar sean iguales.
    while i<= m:
        n1 = randint(0,n) # variable n1 donde selecionara una arista al azar entre 0 y n
        n2 = randint(0,n)  # variable n2 donde selecionara una arista al azar entre 0 y n
        if n1 != n2:
            a = (n1, n2)
            if a not in flag_arista: # SI la arista no se repite o no esta en la lista se crea
                flag_arista[a] = a
                #Crea la arista y la añade al nodo
                GRAFO.Producir_Aristas(aristas.Arista(n1, n2), directed, auto)
            else:
                i = i-1
        else:
            i = i-1
        
        i = i + 1
        
    return GRAFO
