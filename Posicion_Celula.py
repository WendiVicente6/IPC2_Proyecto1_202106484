from ListaDoble_Posicon import Lista_posiciones
class Posicion_Celula():
    def __init__(self, nombre_paciente,edad_paciente,periodos,dimension_x) -> None:
        self.nombre_paciente= nombre_paciente
        self.edad_paciente=edad_paciente
        self.periodos=periodos

        self.dimension_x = dimension_x

        self.procesado = False
        
        self.lista_pos = Lista_posiciones()
        self.siguiente = None