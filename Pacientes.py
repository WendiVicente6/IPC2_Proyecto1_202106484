from DatosPacientes import DatosPaciente
class Matriz():
    def __init__(self) -> None:

        self.size=0
        self.inicio=None
    
    def Crear_Paciente(self,nombre,edad,cantper,m):
        nueva_trayectoria = DatosPaciente(nombre,edad,cantper,m)
        self.size += 1

        if self.inicio is None:
            self.inicio = nueva_trayectoria
        
        else:
            trayectoria_temporal = self.inicio
            while trayectoria_temporal.siguiente is not None:
                trayectoria_temporal  = trayectoria_temporal.siguiente
            trayectoria_temporal.siguiente = nueva_trayectoria      

    def get_Paciente(self, nombre):
        trayectoria_temporal = self.inicio
        while trayectoria_temporal is not None:
            if trayectoria_temporal.edad_paciente == nombre:
                return trayectoria_temporal
            trayectoria_temporal = trayectoria_temporal.siguiente
        return None