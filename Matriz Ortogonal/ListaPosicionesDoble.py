from ast import LtE
import os
from pickle import NONE
from pickletools import read_uint1
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
        self.p=None
        self.q=None
        
    
    def Insertar(self, Px,Py,Dato):
        Insercion=nodoOrtogonal(Dato,Px,Py)
        self.p=Insercion
        
        if self.C.Existe(Px)==False:
            self.C.agregar(Px)

        elif self.F.Existe(Py)==False:
            self.F.agregar(Py)
            
            
        Ctemporal=None
        Ltemporal=None
        Ctemporal=self.C.Buscar(Px)
        Ltemporal=self.F.Buscar(Py)
        Ctemporal.Columna.agregar(self.p.dato,self.p.x,self.p.y)
        Ltemporal.Fila.agregar(self.p.dato,self.p.x,self.p.y)

    
    def Llenar(self,Px,Py,dato):

        for i in range(Px):
            
            for j in range (Py):
                
                
                Nuevo=nodoOrtogonal(dato,i,j)
                self.p=Nuevo
                if(j==0):
                    self.p.izquierdo=None
                    if self.p==None:
                        self.p=self.p
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
                self.r=self.p 
            while self.r.abajo!=None:
                self.r=self.r.abajo
                    
                #self.Insertar(i,j,dato)
    def generar_grafica(self,columnas,nombre):
        graphviz = """
        digraph L{
        node[shape = ellipse fillcolor = "yellow" style = filled]
        

        subgraph cluster_p{
            label = \""""+str(nombre) +"""\"
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

        posiciones =self.p
        
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

        dot = "matriz_{}_dot.dot".format(nombre)
        result = "matriz_{}.png".format(nombre)
        os.system("dot -Tpng " + dot + " -o " + result)
        os.system('cd ./'.format(result))
        os.startfile(dot)

    

        



    