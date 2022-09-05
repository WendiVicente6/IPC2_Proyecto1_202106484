class nodoOrtogonal():



    def __init__(self,x,y,dato,tamaño,posicion_sin_usar):
        self.dato=dato
        self.tamaño=tamaño
        self.x=x
        self.y=y
        self.posicion_sin_usar=posicion_sin_usar
        self.arriba=None
        self.abajo=None
        self.izquierdo=None
        self.derecho=None