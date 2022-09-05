
from NodoCabecera import NodoCabecera



class ListaHorizontal():
    def __init__(self,cof) -> None:
        self.primero:NodoCabecera=None
        self.ultimo:NodoCabecera=None
        self.cof=cof
        self.size=0

    def insertar(self, nuevo):
        self.size +=1
        if self.primero==None:
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            if nuevo.x< self.primero.x:
                nuevo.siguiente=self.primero
                self.primero.Anterior=nuevo
                self.primero=nuevo
            elif nuevo.x > self.ultimo.x:
                self.ultimo.siguiente=nuevo
                nuevo.Anterior=self.ultimo
                self.ultimo=nuevo
            else:
                tmp:NodoCabecera = self.primero
                while tmp!=None:
                    if nuevo.x < tmp.x:
                        nuevo.siguiente=tmp
                        nuevo.Anterior=tmp.Anterior
                        tmp.Anterior.siguiente=nuevo
                        tmp.Anterior=nuevo
                        break
                    elif nuevo.x>tmp.x:
                        tmp=tmp.siguiente
                    else:
                        break

    def mostrarEncabezados(self):
        tmp=self.primero
        while tmp!=None:
            print('Encabezado ', self.cof, tmp.x)
            tmp=tmp.siguiente

    def getEncabezado(self,x)->NodoCabecera:
        tmp=self.primero
        while tmp!= None:
            if x==tmp.x:
                return tmp
            tmp=tmp.siguiente
        return None   