import collections
from graphviz import Digraph
from graphviz import Graph as Graphviz
from clases import aristas
from clases import nodos
import sys

DIRECTED = "DIRECTED"
DISCOVERED = "DISCOVERED"
RENDER = False


class Grafo:
    def __init__(self, num_nodos=None, num_aristas=None, atrbt={}):
        
        if num_nodos is None:
            num_nodos = {}
        self.num_nodos = num_nodos
        
        if num_aristas is None:
            num_aristas = {}
        self.num_aristas = num_aristas
        
        self.atrbt = atrbt
        
    def Arbol_Dijktra(self,nodo):
        vertices = []
        distancia = {}
        flag = {}
        nodo_encontrado = {}
        
        GRAFO = Grafo(atrbt = {DIRECTED: True})
        GRAFO.Producir_Vertices(nodos.Nodo(nodo, {"WEIGHT": 0}))
        
        for nodo_a in self.Dijkstra_Nodos():
            distancia[nodo_a] = float('nodo info')
            flag[nodo_a] = None
            nodo_encontrado[nodos] = False
    
        distancia[nodo] = 0
        vertices.append((nodo, distancia[nodo]))
    
        while len(vertices) != 0:
            nodo_b = min(vertices, key = lambda x: x[1])
            vertices.remove(nodo_b)
            nodo_b = nodo_b[0]
            nodo_encontrado[nodo_b] = True
            for nodo_a in self.Trayectoria_Adyacente(nodo_b):
                if not nodo_encontrado[nodo_a]:
                    v = distancia[nodo_b] + self.Dijkstra_ID((nodo_b,nodo_a)).atrbt["WEIGHT"]
                    if v < distancia[nodo_a]:
                        distancia[nodo_a] = v
                        flag[nodo_a] = nodo_b
                        vertices.append((nodo_a, distancia[nodo_a]))
                        GRAFO.Producir_Vertices(nodos.Nodo(nodo_a, {"WEIGHT": distancia[nodo_a]}))
                        GRAFO.Producir_Aristas(aristas.Arista(nodo_b, nodo_a, {"WEIGHT": distancia[nodo_a]}))
                    
        return GRAFO
        
    def Aristas_Aleatorias(self):
        aristas = []
        for (key, value) in self.num_aristas.keys():
            aristas.append((key, value))
        
        return aristas
    
    
    def BFS(self, s):
        GRAFO_bfs = Grafo(atrbt={DIRECTED: True})
        nodo_seleccionado = self.ID(s)
        nodo_seleccionado.atributos[DISCOVERED] = True
        q = collections.deque()
        t_adyacente = '+' if DIRECTED in self.atrbt and self.atrbt[DIRECTED] else None
        GRAFO_bfs.Producir_Vertices(nodo_seleccionado)
        q.append(s)
        while (len(q) > 0):
            nodo = q.popleft()
            for arista in self.Trayectoria_Adyacente(nodo, t_adyacente):
                conexion = self.ID(arista)
                if DISCOVERED not in conexion.atributos or conexion.atributos[DISCOVERED] is False:
                    conexion.atributos[DISCOVERED] = True
                    q.append(conexion.id)
                    GRAFO_bfs.Producir_Vertices(conexion)
                    GRAFO_bfs.Producir_Aristas(aristas.Arista(nodo, arista), True)
        
        return GRAFO_bfs
    
    def Buscar(self, paridad, nodo_primario):
        if paridad[nodo_primario] == nodo_primario:
            return nodo_primario
        return self.Buscar(paridad, paridad[nodo_primario])
        
    
    def DFS(self, root):
        GRAFO_dfs = Grafo(atrbt={DIRECTED: True})
        t_adyacente = '+' if DIRECTED in self.atrbt and self.atrbt[DIRECTED] else None
        pila = collections.deque()
        pila.append(('#', root))
        while (len(pila) > 0):
            (origen, destino) = pila.pop()
            conexion = self.ID(destino)
            if DISCOVERED not in conexion.atributos or conexion.atributos[DISCOVERED] is False:
                conexion.atributos[DISCOVERED] = True
                GRAFO_dfs.Producir_Vertices(conexion)            
                if (origen != '#'):
                    GRAFO_dfs.Producir_Aristas(aristas.Arista(origen, conexion.id), True)
                for arista in self.Trayectoria_Adyacente(conexion.id,t_adyacente):
                    pila.append((conexion.id, arista))
        
        return GRAFO_dfs 
    
    def DFS_R(self, root):
        GRAFO_dfsr = Grafo(atrbt={DIRECTED: True})
        return self.Recursividad(GRAFO_dfsr, ('#', root)) 
    
    def Dijkstra_ID(self,id,directed = False):
        (nodo_init,nodo_fin) = id
        for (init,fin) in self.num_aristas.keys():
            if directed:
                if (init,fin) == (nodo_init,nodo_fin):
                    return self.num_aristas[(init,fin)]
            
            else:
                if (init,fin) == (nodo_init,nodo_fin) or (init,fin) == (nodo_fin,nodo_init):
                    return self.num_aristas[(init,fin)]
        
        return None
                    
    
    def Dijkstra_Nodos(self):
        return self.num_nodos
    
    
    def Ditto_Kruskal(self):
        RKRUSKAL = Grafo(atrbt = self.atrbt.copy(), num_nodos = self.num_nodos.copy(), num_aristas = self.num_aristas.copy())
        return RKRUSKAL
               
               
    def graphiv(self, n_archivo, atri_nodo = None, source = None, atri_arista = None):
        dot = Graphviz()
        
        # Review attribute directed of graph
        if DIRECTED in self.atrbt:
            if self.atrbt[DIRECTED]:
                dot = Digraph()
            else:
                dot = Graphviz()
        
        if atri_nodo is None:
            for n in list(self.num_nodos.keys()):
                dot.node(str(n), str(n))        
        else:
        # Map graph to graphviz structure and add vertex attribute
            for n in list(self.num_nodos.keys()):
                label = "Nodo actual: " + str(n)
                source_label = "Nodo inicial: " + str(source) if source is not None else ""
                label = label + "\n" + source_label
                label = label + "\n" + atri_nodo + " (" + str(self.num_nodos[n].atributos[atri_nodo]) + ")"
                dot.node(str(n), label)
        
        if atri_arista is None:
            for a in self.Aristas_Aleatorias():
                (s,t) = a
                dot.edge(str(s), str(t))
        else:
            for a in self.Aristas_Aleatorias():
                (s,t) = a
                flag_arista = self.num_aristas[(s,t)].atrbt["WEIGHT"]
                dot.edge(str(s), str(t), label=str(flag_arista))
                
        #file = open("/home/dreadscythe/ED/Programas/Algoritmos/" + n_archivo + ".gv", "w")
        file = open(n_archivo + ".gv", "w")
        file.write(dot.source)
        file.close()
        return dot
    
    def ID(self, id):
        if id in self.num_nodos.keys():
            return self.num_nodos[id]
        else:
            return None
    
    def Kruskal(self):
        
        KRUSKAL = Grafo(atrbt = {DIRECTED:False})
        paridad  = []
        rango = []
        
        for nodo in self.Kruskal_Nodos():
            paridad.append(nodo)
            rango.append(0)
        
        list_aristas = sorted(self.num_aristas.items(), key = lambda arista: arista[1].atrbt["WEIGHT"])
        
        for arista in list_aristas:
            (n_init, nodo_final) = arista[0]
            nodo_primario = self.Buscar(paridad, n_init)
            nodo_secundario = self.Buscar(paridad, nodo_final)
            if nodo_primario != nodo_secundario:
                KRUSKAL.Producir_Vertices(nodos.Nodo(n_init))
                KRUSKAL.Producir_Vertices(nodos.Nodo(nodo_final))
                KRUSKAL.Producir_Aristas(aristas.Arista(n_init,nodo_final,{"WEIGHT": arista[1].atrbt["WEIGHT"]}))
                if rango[nodo_primario] < rango[nodo_secundario]:
                    paridad[nodo_primario] = nodo_secundario
                    rango[nodo_secundario] += 1
                else:
                    paridad[nodo_secundario] = nodo_primario
                    rango[nodo_primario] += 1
        
        return KRUSKAL
    
    
    def Kruskal_Nodos(self):
        return self.num_nodos
    
    def Prim(self):
        PRIM = Grafo(atrbt = {DIRECTED: False})
        distancia = [sys.maxsize] * len(self.num_nodos)
        paridad = [None] * len(self.num_nodos)
        flag = [False] * len(self.num_nodos)
        distancia[124] = 124
        paridad[124] = -1
        
        for nodo in self.num_nodos:
            distancia_minima = 124
            min = sys.maxsize
            for nodo_b in self.num_nodos:
                if distancia[nodo_b] < min and flag[nodo_b] is False:
                    min = distancia[nodo_b]
                    distancia_minima = nodo_b
            
            nodo_a = distancia_minima
            flag[nodo_a] = True
            PRIM.Producir_Vertices(nodos.Nodo(nodo_a))
            
            for nodo_b in self.Trayectoria_Adyacente(nodo_a):
                if flag[nodo_b] is False and distancia[nodo_b] > self.Prim_ID((nodo_a, nodo_b)).atrbt["WEIGHT"]:
                    distancia[nodo_b] = self.Prim_ID((nodo_a, nodo_b)).atrbt["WEIGHT"]
                    paridad[nodo_b] = nodo_a
        
        for nodo in self.num_nodos:
            if nodo  == 124:
                continue
            if paridad[nodo] is not None:
                PRIM.Producir_Aristas(aristas.Arista(paridad[nodo], nodo, {"WEIGHT": self.Prim_ID((paridad[nodo], nodo)).atrbt["WEIGHT"]}))    
        
        return PRIM
        
    def Prim_ID(self,id,directed = False):
        (nodo_init,nodo_fin) = id
        for (init,fin) in self.num_aristas.keys():
            if directed:
                if (init,fin) == (nodo_init,nodo_fin):
                    return self.num_aristas[(init,fin)]
         
            else:
                if (init,fin) == (nodo_init,nodo_fin) or (init,fin) == (nodo_fin,nodo_init):
                    return self.num_aristas[(init,fin)]
     
        return None
                
            
        
    def Producir_Aristas(self, arista, directed = False, auto = False):    
        (nodo_a, nodo_b) = arista.P2P()
        if nodo_a in self.num_nodos.keys() and nodo_b in self.num_nodos.keys():
            if directed:
                if auto:
                    self.num_aristas[arista.P2P()] = arista
                else:
                    if nodo_a != nodo_b:
                        self.num_aristas[arista.P2P()] = arista
            else:
                if self.num_aristas.get((nodo_b, nodo_a)) is None:
                    if auto:
                        self.num_aristas[arista.P2P()] = arista
                    else:
                        if nodo_a != nodo_b:
                            self.num_aristas[arista.P2P()] = arista
    
    
    def Producir_Vertices(self,v):
        if v.id not in self.num_nodos.keys():
            self.num_nodos[v.id] = v
    
    
    
    def Recursividad(self, GRAFO_dfsr, root):
        t_adyacente = '+' if DIRECTED in self.atrbt and self.atrbt[DIRECTED] else None
        (origen, destino) = root
        conexion = self.ID(destino)
        if DISCOVERED not in conexion.atributos or conexion.atributos[DISCOVERED] is False:
            conexion.atributos[DISCOVERED] = True
            GRAFO_dfsr.Producir_Vertices(conexion)
            if (origen != '#'):
                GRAFO_dfsr.Producir_Aristas(aristas.Arista(origen, conexion.id), True)
            
            for arista in self.Trayectoria_Adyacente(conexion.id, t_adyacente):
                self.Recursividad(GRAFO_dfsr, (conexion.id, arista))
        
        return GRAFO_dfsr   
    
    def Trayectoria_Adyacente(self, id, type=None):
        nodos = []
        for (inicio, arribo) in self.num_aristas.keys():
            if type is None:
                if inicio == id:
                    nodos.append(arribo)
                elif arribo == id:
                    nodos.append(inicio)
            elif type == '+':
                if inicio == id:
                    nodos.append(arribo)
            elif type == '-':
                if arribo == id:
                    nodos.append(inicio)
        return nodos
    
    def Trayectoria_Normal(self, id, type =0):
        aristas = []
        for (inicio, arribo) in self.num_aristas.keys():
            if type == 1:
                if inicio == id:
                    aristas.append((inicio, arribo))
            elif type == 2:
                if arribo == id:
                    aristas.append((inicio, arribo))
            else:
                if inicio == id or arribo == id:
                    aristas.append((inicio, arribo))
        
        return aristas

    
    def Recursividad(self, GRAFO_dfsr, root):
        t_adyacente = '+' if DIRECTED in self.atrbt and self.atrbt[DIRECTED] else None
        (origen, destino) = root
        conexion = self.ID(destino)
        if DISCOVERED not in conexion.atributos or conexion.atributos[DISCOVERED] is False:
            conexion.atributos[DISCOVERED] = True
            GRAFO_dfsr.Producir_Vertices(conexion)
            if (origen != '#'):
                GRAFO_dfsr.Producir_Aristas(aristas.Arista(origen, conexion.id), True)
                
            for arista in self.Trayectoria_Adyacente(conexion.id, t_adyacente):
                self.Recursividad(GRAFO_dfsr, (conexion.id, arista))
        
        return GRAFO_dfsr
    
    
    def Reverso_Kruskal(self):
        R_KRUSKAL = self.Ditto_Kruskal()
        l = sorted(self.num_aristas.items(), key = lambda a: a[1].atrbt["WEIGHT"], reverse = True)
        for a in l:
            R_KRUSKAL.num_aristas.pop(a[0])
        
            for nodo in self.num_nodos:
                R_KRUSKAL.num_nodos[nodo].atributos["DISCOVERED"] = False
            
            if len(R_KRUSKAL.num_nodos) != len(R_KRUSKAL.BFS(0).num_nodos):
                R_KRUSKAL.Producir_Aristas(a[1])
        
        return R_KRUSKAL
    

    
    def Dijkstra(self, nodo_inicial, nodo_final):
        vertices = []
        distancia= {}
        flag = {}
        nodo_encontrado = {}
        
        for nodo in self.Dijkstra_Nodos():
            distancia[nodo] = float('inf')
            flag[nodo] = None
            nodo_encontrado[nodo] = False
        
        distancia[nodo_inicial] = 0
        vertices.append((nodo_inicial, distancia[nodo_inicial]))
        
        while len(vertices) != 0:
            nodo_b = min(vertices, key = lambda x:x[1])
            vertices.remove(nodo_b)
            nodo_b = nodo_b[0]
            nodo_encontrado[nodo_b] = True
            
            if nodo_b == nodo_final:
                break
            
            for nodo in self.Trayectoria_Adyacente(nodo_b):
                if not nodo_encontrado[nodo]:
                    v = distancia[nodo_b] + self.Dijkstra_ID((nodo_b,nodo)).atrbt["WEIGHT"]
                    if v < distancia[nodo]:
                        distancia[nodo] = v
                        flag[nodo] = nodo_b
                        vertices.append((nodo,distancia[nodo]))  
        
        
        nodo_b = nodo_final
        GRAFO = Grafo(atrbt={DIRECTED:True})
        while nodo_b is not None:
            GRAFO.Producir_Vertices(nodos.Nodo(nodo_b,{"WEIGHT": distancia[nodo_b]}))
            if flag[nodo_b] is not None:
                GRAFO.Producir_Vertices(nodos.Nodo(flag[nodo_b], {"WEIGHT":distancia[flag[nodo_b]]}))
                GRAFO.Producir_Aristas(aristas.Arista(flag[nodo_b],nodo_b))
                nodo_b = flag[nodo_b]
            else:
                break
        
        return GRAFO
    
    




                