from NodoOrtogonal import nodoOrtogonal
class ListaVertical():
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
            if (Nuevo.y<self.primero.y):
                self.primero.arriba=Nuevo
                Nuevo.abajo=self.primero
                self.primero=self.primero.arriba
            elif (Nuevo.y>self.ultimo.y):
                self.ultimo.abajo=Nuevo
                Nuevo.arriba=self.ultimo
                self.ultimo=self.ultimo.abajo
            else:
                temporal1=self.primero
                while(temporal1.y<Nuevo.y):
                    temporal1=temporal1.abajo
                temporal2=temporal1.arriba
                temporal2.abajo=Nuevo
                temporal1.arriba=Nuevo
                Nuevo.abajo=temporal1
                Nuevo.arriba=temporal2
                
                
                

    def recorrer(self):
        aux = self.primero
        while(aux !=None):
            print("Y: ",aux.y)
            aux=aux.abajo


            
