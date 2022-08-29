from Posicion import Posicion
class Lista_posiciones():
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.tamano = 0
    
    def insertar(self, posicion_c, posicion_f,  posicion_sin_usar, posicion_2D):
        nueva_posicion = Posicion(posicion_c, posicion_f,  posicion_sin_usar, posicion_2D)
        self.tamano += 1

        if self.inicio is None:
            self.inicio = nueva_posicion
        else:
            temporal = self.inicio

            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nueva_posicion
            self.fin = nueva_posicion
            nueva_posicion.anterior = temporal

    def mostrar_posiciones(self):
        temporal = self.inicio
        grafica = ""
        while temporal is not None:
            grafica += temporal.posicion_2D
            temporal = temporal.siguiente

        return grafica

    def mostrar(self):
        temporal = self.inicio
        grafica = ""
        while temporal is not None:
            grafica += ("("+ str(temporal.posicion_c)+ "," + str(temporal.posicion_f)+")")
            temporal = temporal.siguiente
        #grafica = grafica[::-1]
        return grafica 

    def get_posicion(self, posicionx, posiciony):
        posicion = self.inicio
        while posicion is not None:
            if posicionx == posicion.posicion_c and posiciony == posicion.posicion_f:
                return posicion
            posicion = posicion.siguiente
        return None


    
    def camino(self):
        posicion=self.inicio
        while posicion is not None:
            posicion.posicion_2D = "|1|"
            posicion = self.get_posicion(posicion.predecesor_x, posicion.predecesor_y)