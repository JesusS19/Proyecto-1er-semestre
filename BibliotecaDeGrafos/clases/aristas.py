

"""
Clase Arista: Se ingresa a la clase Arista, dos attributos tipo int (inicio,destino), donde equivalen 
al nodo virtual inicial y nodo virtual destino.
"""

class Arista:
    def __init__(self,inicio,arribo,atrbt=None):
        
        self.inicio = inicio #Objeto nodo inicial
        self.arribo = arribo #Objeto nodo destino
        self.arista = (inicio, arribo) # Objeto arista crea la trayectoria de nuestras variablesrbt
        
        if atrbt is None:
            self.atrbt = {}
        else:
            self.atrbt = atrbt
    
    def P2P(self): # Funcion Point to Point
        """
        En esta funcion se regresara nuestro variable virtual (arista) que incluye los datos d ela trayectoria 
        que se creo a los nodos que se le ingresaron (inicio,destino).
        """
        return self.arista
    
    



        

    