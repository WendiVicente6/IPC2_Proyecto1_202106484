from ast import LtE
import os
from pickle import NONE
import webbrowser
from ListaHorizontalSimple import ListaHorizontal
from NodoCabecera import Cabeceras, NodoCabecera
from NodoLaterales import Laterales
from NodoOrtogonal import nodoOrtogonal
from graphviz import Digraph

class MatrizOrtogonal():
    def __init__(self) -> None:
        '''self.size=size

        self.vacias=-1
        self.tamaño=0'''
        self.C=Cabeceras()
        self.F=Laterales()
        self.primero=None
        self.p=None
        self.q=None
        
    
    def Insertar(self, Px,Py,Dato):
        Insercion=nodoOrtogonal(Dato,Px,Py)
        self.primero=Insercion
        if self.C.Existe(Px)==False:
            self.C.agregar(Px)

        if self.F.Existe(Py)==False:
            self.F.agregar(Py)

        Ctemporal=None
        Ltemporal=None
        Ctemporal=self.C.Buscar(Px)
        Ltemporal=self.F.Buscar(Py)
        Ctemporal.Columna.agregar(self.primero.dato,self.primero.x,self.primero.y)
        Ltemporal.Fila.agregar(self.primero.dato,self.primero.x,self.primero.y)

    
    def Llenar(self,Px,Py,dato):

        for i in range(Px):
            for j in range (Py):
                Nuevo=nodoOrtogonal(dato,Px,Py)
                self.p=Nuevo
                if(j==0):
                    self.p.izquierdo=None
                    if self.primero==None:
                        self.primero=self.p
                    self.q=self.p
                else:
                    self.p.izquierdo=self.q
                    self.q.derecho=self.p
                    self.q=self.p
                if (i==0):
                    self.p.arriba=None
                    self.q=self.p
                else:
                    self.p.arriba=self.r 
                    self.r.abajo=self.p
                    self.r=self.r.derecho
            self.r=self.primero 
            while self.r.abajo!=None:
                self.r=self.r.abajo
                    
                #self.Insertar(i,j,dato)
    def generar_grafica(self,columnas):
        graphviz = """
        digraph L{
        node[shape = ellipse fillcolor = "yellow" style = filled]
        

        subgraph cluster_p{
            label = \""""+"Prueba" +"""\"
            bgcolor = "white"
            raiz[label = "F/C"]
            edge[dir = "none"]
            /*Aqui creamos las cabeceras de las filas */
            """ 
        filas = ""
        for i in range(1,columnas+ 1):
            filas += "Fila"+ str(i) +"[label = \""+ str(i) + """\", group = 1];\n""" 
        
        for i in range(1, columnas):
            filas += """Fila"""+ str(i) +"""->Fila"""+str(i+1)+";\n"
        
        graphviz += filas

        Colum = ""
        for i in range(1, columnas + 1):
            Colum += "Columna"+ str(i) +"[label = \""+ str(i) + """\", group = """+str(i+1) +", fillcolor = yellow];\n""" 

        for i in range(1, columnas):
            Colum += "Columna"+ str(i) +"->Columna"+str(i+1)+";\n"
            
        graphviz += Colum

        graphviz += """raiz -> Fila1;
        raiz -> Columna1;
        {rank = same; raiz; """
        
        rank = ""
        for i in range(1, columnas + 1):
            rank += "Columna"+ str(i) +";"
        
        graphviz += rank
        graphviz += "}"

        posiciones =self.primero
        
        nodo = ""
        while posiciones is not None:
            if posiciones.dato == '|1|':
                nodo += "nodo"+ str(posiciones.x) +"_"+ str(posiciones.y) +"[label=\""+str(posiciones.x)+","+str(posiciones.y)+"\", fillcolor = red, group = "+str((posiciones.y + 1))+"]\n"
                posiciones = posiciones.derecho


            else:
                nodo += "nodo"+ str(posiciones.x) +"_"+ str(posiciones.y) +"[label=\""+str(posiciones.x)+","+str(posiciones.y)+"\", fillcolor = green, group = "+str((posiciones.y + 1))+"]\n"
                posiciones = posiciones.derecho


        graphviz += nodo

        for i in range(1, columnas + 1):
            graphviz += "{rank = same; Fila"+str(i)+";"
            for j in range(1, columnas + 1):
                graphviz += "nodo"+str(i)+"_"+str(j)+";"
                if columnas == j and columnas!= i:
                    graphviz += "}\n"

        graphviz += "}"

        for j in range(1, columnas+ 1):
                graphviz += "Fila"+str(j)+"->"+"nodo"+str(j)+"_"+str(1)+";"

        for j in range(1, columnas+ 1):
                graphviz += "Columna"+str(j)+"->"+"nodo"+str(1)+"_"+str(j)+";"


        for i in range(1, columnas):
            for j in range(1, columnas + 1):
                graphviz += ("nodo"+str(i)+"_"+str(j)+"-> nodo"+str(i+1)+"_"+str(j)+";\n")

        for i in range(1, columnas+ 1):
            for j in range(1,  columnas):
                graphviz += ("nodo"+str(i)+"_"+str(j)+"-> nodo"+str(i)+"_"+str(j+1)+";\n")

        
        graphviz += """}
        }""" 

        miArchivo = open('graphviz.dot', 'w')
        miArchivo.write(graphviz)
        miArchivo.close()
        os.system('dot -Tpng graphviz.dot -o graphviz.png')
        os.system('cd ./graphviz.png')
        os.startfile('graphviz.png')

    

        



    