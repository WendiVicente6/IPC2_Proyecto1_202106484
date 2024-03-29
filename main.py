from operator import truediv

import xml.etree.ElementTree as ET
from Pacientes import Matriz



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
        listatejido.Crear_Paciente(tamaño,nombre,edad,cantper,)

        for rejilla in elem.iter('rejilla'):
            tejido=listatejido.get_Paciente(nombre)
            for posicion in rejilla.iter('celda'):
                
                columna=int(posicion.attrib['c'])
                fila=int(posicion.attrib['f'])
                print('C y F:',columna,fila)
                tejido.lista_posiciones.Insertar(fila,columna,"|0|",posicion_sin_usar)
            tejido.lista_posiciones.Llenar(tamaño,tamaño,"|1|",posicion_sin_usar)
            tejido.lista_posiciones.graficarDibujo("TEJIDOS")

def menu():
    print("")
    
    print("")
    
    opcion = ''
    matriz=Matriz()


    
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