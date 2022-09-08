from NodoOrtogonal import nodoOrtogonal

class ListaHorizontal():
    def __init__(self) -> None:
        self.primero=None
        self.ultimo=None

    def vacio(self):
        if self.primero==None:
            return True
        else: 
            return False

    def agregar(self,dato,x,y):
        Nuevo = nodoOrtogonal(dato,x,y)
        
        if self.vacio():
            self.primero = self.ultimo = Nuevo
        else:
            if (Nuevo.x<self.primero.x):
                self.primero.izquierdo=Nuevo
                Nuevo.derecho=self.primero
                self.primero=self.primero.izquierdo
            elif (Nuevo.x>self.ultimo.x):
                self.ultimo.derecho=Nuevo
                Nuevo.izquierdo=self.ultimo
                self.ultimo=self.ultimo.derecho
            else:
                temporal1=self.primero
                while(temporal1.x<Nuevo.x):
                    temporal1=temporal1.derecho
                temporal2=temporal1.izquierdo
                temporal2.derecho=Nuevo
                temporal1.izquierdo=Nuevo
                Nuevo.derecho=temporal1
                Nuevo.izquierdo=temporal2
                
    def recorrer(self):
        aux = self.primero
        while(aux !=None):
            print("X: ",aux.x)
            aux=aux.derecho
    