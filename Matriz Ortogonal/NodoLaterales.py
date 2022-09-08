from distutils.log import FATAL
from ListaHorizontalSimple import ListaHorizontal


class NodoLateral():
    def __init__(self,y) -> None:
        self.y=y
        self.Siguiente=None
        self.Anterior=None
        self.Fila=ListaHorizontal()

class Laterales():
    def __init__(self) -> None:
        self.primero=None
        self.ultimo=None
        self.Fila=None

    def vacio(self):
        if self.primero == None:
            return True
        else:
            return False

    def agregar(self,y):
        Nuevo = NodoLateral(y)
        
        if self.vacio():
            self.primero = self.ultimo = Nuevo
        else:
            if (Nuevo.y<self.primero.y):
                self.primero.Anterior=Nuevo
                Nuevo.Siguiente=self.primero
                self.primero=self.primero.Anterior
            elif (Nuevo.y>self.ultimo.y):
                self.ultimo.Siguiente=Nuevo
                Nuevo.Anterior=self.ultimo
                self.ultimo=self.ultimo.Siguiente
            else:
                temporal1=self.primero
                while(temporal1.y<Nuevo.y):
                    temporal1=temporal1.Siguiente
                temporal2=temporal1.Anterior
                temporal2.Siguiente=Nuevo
                temporal1.Anterior=Nuevo
                Nuevo.Siguiente=temporal1
                Nuevo.Anterior=temporal2
                

    def recorrer(self):
        aux = self.primero
        while(aux is not None):
            print("Y: ",aux.y)
            aux = aux.Siguiente
            

    def Existe(self,y):
        if(self.vacio==False):
            return False
        else:
            temporal=self.primero
            while(temporal!=None):
                if(temporal.y==y):

                    return True
                elif(temporal.Siguiente==None):

                    return False
                temporal=temporal.Siguiente
        
    def Buscar(self, y):
        if(self.Existe(y)):
            temporal=self.primero
            while (temporal.y!=y):
                temporal=temporal.Siguiente
            return temporal
        else:

            return NodoLateral(-1)   