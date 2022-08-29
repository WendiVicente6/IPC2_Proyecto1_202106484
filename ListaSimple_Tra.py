
from Posicion_Celula import Posicion_Celula


class ListaPatrones():
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.size =0
    

    def crear_tejido(self,nombre,edad,cantper,m):
        nueva_trayectoria = Posicion_Celula(nombre,edad,cantper,m)
        self.size += 1

        if self.inicio is None:
            self.inicio = nueva_trayectoria
        
        else:
            trayectoria_temporal = self.inicio
            while trayectoria_temporal.siguiente is not None:
                trayectoria_temporal  = trayectoria_temporal.siguiente
            trayectoria_temporal.siguiente = nueva_trayectoria

    
    def get_tejido(self, nombre):
        trayectoria_temporal = self.inicio
        while trayectoria_temporal is not None:
            if trayectoria_temporal.nombre_paciente == nombre:
                return trayectoria_temporal
            trayectoria_temporal = trayectoria_temporal.siguiente
        return None


    def imprimir_terrenos(self):
        terreno = self.inicio
        contador = 1
        while terreno is not None:
            print(str(contador) + ". " + terreno.nombre_paciente)
            contador += 1
            terreno = terreno.siguiente
        return None
