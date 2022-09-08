from ListaHorizontalSimple import ListaHorizontal
from ListaPosicionesDoble import MatrizOrtogonal
from ListasVerticalesSimple import ListaVertical
from ListaSimplePaciente import Matriz


import xml.etree.ElementTree as ET
from NodoCabecera import Cabeceras, NodoCabecera

from NodoOrtogonal import nodoOrtogonal




def cargar_archivo(mostrar,listatejido):
    tree = ET.parse(mostrar)
    root = tree.getroot()
    posicion_sin_usar=True
    
    for elem in root:
        global tamaño
        fila = 0
        columna = 0
        tamaño = 0
        cantper  = 0 
        
        print('Paciente')
        for paciente in elem.iter('datospersonales'):
            for nombre in paciente.iter('nombre'):
                nombre=nombre.text
                
                print('Nombre Paciente: ',nombre)
            for edad in paciente.iter('edad'):
                edad=edad.text
                print('Edad paciente: ',edad)
        for periodo in elem.iter('periodos'):
            cantper=int(periodo.text)
            print('Cantidad Periodos: ',cantper)
        for m in elem.iter('m'):
            tamaño=int(m.text)
            print('Tamaño Tejido:' ,tamaño)
        listatejido.Crear_Paciente(tamaño,nombre,edad,cantper)

        for rejilla in elem.iter('rejilla'):
            tejido=listatejido.get_Paciente(nombre)
            tejido.lista_posiciones.Llenar(tamaño,tamaño,"|0|")
            for posicion in rejilla.iter('celda'):
                
                columna=int(posicion.attrib['c'])
                fila=int(posicion.attrib['f'])
                tejido.lista_posiciones.Insertar(fila,columna,"|1|")
            #tejido.lista_posiciones.Matriz()
            tejido.lista_posiciones.generar_grafica(tamaño,nombre)
            #tejido.lista_posiciones.graficarDot("Hola")





                  
def menu():
    print("")
    
    print("")
    
    opcion = ''
    matriz=Matriz()
    #grafica=MatrizPosicioness(0)
    listavertical=MatrizOrtogonal()
   
    while opcion != '6':
        print("")
        print("""Menú principal:
        1. Cargar archivo
        6. Salida
        """)

        opcion = input("Ingrese una opcion: ")

        
        if opcion == '1':
            filename = input("Ingrese el archivo: ")
            file = './' + filename
            cargar_archivo(file,matriz)
        if opcion == '2':
            pass
            
            
            #lista.imprimir_terrenos()

        elif opcion != '6':
            print("Opcion incorrecta\n")

        


if __name__ == '__main__':
    menu()
