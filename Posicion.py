class  Posicion():
    def __init__(self, posicion_c, posicion_f, posicion_sin_usar, posicion_2D) -> None:
        self.posicion_c = posicion_c
        self.posicion_f = posicion_f
        self.posicion_sin_usar = posicion_sin_usar 
        self.posicion_2D = posicion_2D
        self.predecesor_x = None
        self.predecesor_y = None
        self.siguiente = None
        self.anterior = None