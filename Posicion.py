class nodoOrtogonal():



    def __init__(self,dx,dy,dato,posicion_sin_usar):
        self.dato=dato

        self.dx=dx
        self.dy=dy
        self.posicion_sin_usar=posicion_sin_usar
        self.arriba=None
        self.abajo=None
        self.izquierdo=None
        self.derecho=None