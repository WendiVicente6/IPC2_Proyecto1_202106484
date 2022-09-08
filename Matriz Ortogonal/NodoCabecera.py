from math import fabs
from pickle import FALSE, TRUE
from ListasVerticalesSimple import ListaVertical



class NodoCabecera():
    def __init__(self,x):
        self.x=x
        self.Siguiente=None
        self.Anterior=None
        self.Columna=ListaVertical()


class Cabeceras():
    def __init__(self) -> None:
        self.primero=None
        self.ultimo=None

    def vacio(self):
        if self.primero==None:
            return True
        else: 
            return False
    def Existe(self,x):
        if(self.vacio==False):
            return False
        else:
            temporal=self.primero
            while(temporal!=None):
                if(temporal.x==x):
                    print("Encontrado")
                    return True
                elif(temporal.Siguiente==None):
                    return False
                temporal=temporal.Siguiente

    def agregar(self,x):
        Nuevo = NodoCabecera(x)
        
        if self.vacio():
            self.primero = self.ultimo = Nuevo
        else:
            if (Nuevo.x<self.primero.x):
                self.primero.Anterior=Nuevo
                Nuevo.Siguiente=self.primero
                self.primero=self.primero.Anterior
            elif (Nuevo.x>self.ultimo.x):
                self.ultimo.Siguiente=Nuevo
                Nuevo.Anterior=self.ultimo
                self.ultimo=self.ultimo.Siguiente
            else:
                temporal1=self.primero
                while(temporal1.x<Nuevo.x):
                    temporal1=temporal1.Siguiente
                temporal2=temporal1.Anterior
                temporal2.Siguiente=Nuevo
                temporal1.Anterior=Nuevo
                Nuevo.Siguiente=temporal1
                Nuevo.Anterior=temporal2
                
    def recorrer(self):
        aux = self.primero
        while(aux !=None):
            print("X: ",aux.x)
            aux=aux.Siguiente  
              
  
    
    def Buscar(self, x):
        if(self.Existe(x)):
            temporal=self.primero
            while (temporal.x!=x):
                temporal=temporal.Siguiente
            return temporal
        else:

            return NodoCabecera(-1)   
   
