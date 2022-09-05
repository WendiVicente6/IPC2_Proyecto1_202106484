from ListaDoble_Posicon import MatrizPosicioness


class DatosPaciente():
    def __init__(self, nombre_paciente,edad_paciente,periodos,dimension_x) -> None:
        self.nombre_paciente= nombre_paciente
        self.edad_paciente=edad_paciente
        self.periodos=periodos

        self.dimension_x = dimension_x
        self.dimension_y=dimension_x
        
        self.procesado = False

        self.siguiente = None
        self.lista_posiciones=MatrizPosicioness(0)
