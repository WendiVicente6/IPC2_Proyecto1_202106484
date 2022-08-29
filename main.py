from operator import truediv
from tkinter import Menu, filedialog
from xml.dom import minidom
import xml.etree.ElementTree as ET
from ListaSimple_Tra import ListaPatrones

def cargar_archivo(mostrar,listatejido):
    tree = ET.parse(mostrar)
    root = tree.getroot()
    celula_no=True

    for elem in root:
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
        listatejido.crear_tejido(nombre,edad,cantper,tamaño)

        for rejilla in elem.iter('rejilla'):
            
            for posicion in rejilla.iter('celda'):
                tejido=listatejido.get_tejido('AriGameplays')
                columna=int(posicion.attrib['c'])
                fila=int(posicion.attrib['f'])
                print('C y F:',columna,fila)
                tejido.lista_pos.insertar(columna,fila,celula_no,"|0|")

def calculo(trayectorias):
    terreno = trayectorias.inicio

    while terreno is not None:
        if not terreno.procesado:
            print("Nombre del terreno: ", terreno.nombre_paciente)
            terreno.posicion_2D = "|1|"

            dimencion_x = terreno.dimension_x

            #terreno.lista_pos.dijkstra(dimencion_x)
            terreno.lista_pos.camino()
            
            grafica = terreno.lista_pos.mostrar_posiciones()
            dimension = terreno.dimension_x
            longitud = 2*terreno.dimension_x

            #print(grafica)

            for i in range(0, dimension + 1):
                print(grafica[(i-1)*longitud:(i)*longitud])
            """
            grafica = terreno.lista_posiciones.mostrar_posiciones()
            dimension = terreno.dimension_y
            longitud = 3 * terreno.dimension_x
            #print(grafica)
            for i in range(1, dimension + 1):
                print(grafica[(i-1)*longitud:i*longitud])
            """
            print("")
            terreno.procesado = True
        terreno = terreno.siguiente
       
    
   
def menu():
    print("")
    
    print("")
    
    opcion = ''
    lista = ListaPatrones()
    
    while opcion != '6':
        print("")
        print("""Menú principal:
        1. Cargar archivo
        2. Procesar archivo
        3. Escribir archivo XML de salida 
        4. Mostrar datos del estudiante
        5. Generar gráfica
        6. Salida
        """)

        opcion = input("Ingrese una opcion: ")

        
        if opcion == '1':
            filename = input("Ingrese el archivo: ")
            file = './' + filename
            cargar_archivo(file,lista)
        if opcion == '2':
            calculo(lista)
            #lista.imprimir_terrenos()

        elif opcion != '6':
            print("Opcion incorrecta\n")

        


if __name__ == '__main__':
    menu()