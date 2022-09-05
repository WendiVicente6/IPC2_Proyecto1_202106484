class NodoCabecera():
    def __init__(self,x):
        self.x:int=x
        self.siguiente=None
        self.Anterior=None
        self.Columna=None

class Cabeceras():
    def __init__(self) -> None:
        self.primero=None
        self.ultimo=None
        self.Columna=None

    def vacio(self):
        return self.primero == None

    def agregar(self,x):
        Nuevo = NodoCabecera(x)
        
        if self.vacio():
            self.primero = self.ultimo = Nuevo
        else:
            if (Nuevo.x<self.primero.x):
                self.primero.Anterior=Nuevo
                Nuevo.siguiente=self.primero
                self.primero=self.primero.Anterior
            elif (Nuevo.x>self.ultimo.x):
                self.ultimo.siguiente=Nuevo
                Nuevo.Anterior=self.ultimo
                self.ultimo=self.ultimo.siguiente
            else:
                temporal1=self.primero
                while(temporal1.x<Nuevo.x):
                    temporal1=temporal1.siguiente
                temporal2=temporal1.Anterior
                temporal2.siguiente=Nuevo
                temporal1.Anterior=Nuevo
                Nuevo.siguiente=temporal1
                Nuevo.Anterior=temporal2
                

    def recorrer(self):
        aux = self.primero
        while(aux is not None):
            print("X: ",aux.x)
            aux = aux.siguiente
            
    def insertarFrente(self):
        Nuevo=self.primero
        self.primero.Anterior=Nuevo
        Nuevo.siguiente=self.primero
        self.primero=self.primero.Anterior
    
    def Existe(self,x):
        if(self.vacio==False):
            return False
        else:
            temporal=self.primero
            while(temporal!=None):
                if(temporal.x==x):
                    return True
                elif(temporal.siguiente==None):
                    return False
                temporal=temporal.siguiente
    
    def Buscar(self, x):
        if(self.Existe(x)):
            temporal=self.primero
            while (temporal.x!=x):
                temporal=temporal.siguiente
            return temporal
        else:

            return NodoCabecera(-1)   
    def mostrar_posiciones(self):
        temporal = self.primero
        grafica = ""
        while temporal is not None:
            grafica += temporal.x
            temporal = temporal.siguiente
        #grafica = grafica[::-1]
        return grafica