
"""
Clase Nodo que crea m nodos que deseamos ingresar.
"""

class Nodo:
    def __init__(self, id, atributos = None): 
        
        self.id = id

        if atributos is None:
            self.atributos = {}
            
        else:
            self.atributos = atributos
    
    def __repr__(self):
         return f'{id}'
    

        



