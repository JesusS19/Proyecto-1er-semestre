
from clases import nodos
from clases import aristas
from clases import grafo
import math
from random import random


# Coordenadas
cord_x = "x"
cord_y = "y"
"""
Funcio que genera un grafo con nodos aleatorios y sus aristas son con una distancia de r o menor
a la que el usuario ingreso. 
"""
def Geo_S(n, r, directed = False, auto = False):
    GRAFO = grafo.Grafo()
    GRAFO.atrbt[grafo.DIRECTED] = directed
    #Iteracion que produce n nodosen el grafo
    for nodo in range(n):
        GRAFO.Producir_Vertices(nodos.Nodo(nodo,{cord_x: random(), cord_y: random()}))
    #Iteracion donde se busca que la distancia entre nodos se igual o menor a la que ingreso el usuario
    for i in range(n):
        for j in range(n):
            valores1 = (GRAFO.ID(i).atributos[cord_x], GRAFO.ID(i).atributos[cord_y])
            valores2 = (GRAFO.ID(j).atributos[cord_x], GRAFO.ID(j).atributos[cord_y])
            d = distancia(valores1, valores2)
            if d <= r:
                # Crea la arista si la distancia es la deseada
                GRAFO.Producir_Aristas(aristas.Arista(i,j), directed, auto)
    
    return GRAFO
            

#Funcion Basica que calcula la distancia de un punto a otro. 
def distancia(valores1, valores2):
    x1, y1 = valores1
    x2, y2 = valores2
    d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    return d



  