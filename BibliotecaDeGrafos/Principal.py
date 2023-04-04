
from clases.grafo import Grafo
from clases import Modelo_Barabasi, Modelo_Malla
from clases import Modelo_Erdos_Rengy
from clases import Modelo_G_Aleatorio
from clases import Modelo_Geo_S
from clases import Modelo_Dorogo_M
from clases import Modelo_Barabasi


#Modelo Malla
GRAFO = Modelo_Malla.Malla(6,5)
dot = GRAFO.graphiv("Modelo Malla 30")

GRAFO = Modelo_Malla.Malla(10,10)
dot = GRAFO.graphiv("Modelo Malla 100")

GRAFO = Modelo_Malla.Malla(25,20)
dot = GRAFO.graphiv("Modelo Malla 500")

#Modelos Erdos
GRAFO = Modelo_Erdos_Rengy.Erdos_Renyi(30, 30, directed = False, auto = False)
dot = GRAFO.graphiv("Modelo Erdos 30")

GRAFO = Modelo_Erdos_Rengy.Erdos_Renyi(100, 100, directed = False, auto = False)
dot = GRAFO.graphiv("Modelo Erdos 100")

GRAFO = Modelo_Erdos_Rengy.Erdos_Renyi(500, 500, directed = False, auto = False)
dot = GRAFO.graphiv("Modelo Erdos 500")
#Modelo Gilbert
GRAFO = Modelo_G_Aleatorio.Grafo_A(30)
dot = GRAFO.graphiv("Modelo Gilbert 30")

GRAFO = Modelo_G_Aleatorio.Grafo_A(100)
dot = GRAFO.graphiv("Modelo Gilbert 100")

GRAFO = Modelo_G_Aleatorio.Grafo_A(500)
dot = GRAFO.graphiv("Modelo Gilbert 500")

#Modelo Geo simple
GRAFO = Modelo_Geo_S.Geo_S(30, 0.2, directed= False, auto = False)
dot = GRAFO.graphiv("Modelo Geo simple 30")

GRAFO = Modelo_Geo_S.Geo_S(100, 0.2, directed= False, auto = False)
dot = GRAFO.graphiv("Modelo Geo simple 100")

GRAFO = Modelo_Geo_S.Geo_S(500, 0.2, directed= False, auto = False)
dot = GRAFO.graphiv("Modelo Geo simple 500")

#Modelo Barabasi
GRAFO = Modelo_Barabasi.Barabasi(30,15,directed=False, auto=False)
dot = GRAFO.graphiv("Modelo Barabasi 30")

GRAFO = Modelo_Barabasi.Barabasi(100,15,directed=False, auto=False)
dot = GRAFO.graphiv("Modelo Barabasi 100")

GRAFO = Modelo_Barabasi.Barabasi(500,15,directed=False, auto=False)
dot = GRAFO.graphiv("Modelo Barabasi 500")

#Modelo Dorogo
GRAFO = Modelo_Dorogo_M.Dorogo_M(30, directed= False)
dot = GRAFO.graphiv("Modelo Dorogo 30")

GRAFO = Modelo_Dorogo_M.Dorogo_M(100, directed= False)
dot = GRAFO.graphiv("Modelo Dorogo 100")

GRAFO = Modelo_Dorogo_M.Dorogo_M(500, directed= False)
dot = GRAFO.graphiv("Modelo Dorogo 500")




 
