import os
import webbrowser
from ListaSimple_Tra import ListaHorizontal
from NodoCabecera import NodoCabecera
from Posicion import nodoOrtogonal

class MatrizPosicioness():
    def __init__(self,size) -> None:
        self.size=size
        self.filas = ListaHorizontal('fila')
        self.columnas = ListaHorizontal('columna')
        self.vacias=0
        self.primero=None

    def Insertar(self, pos_x, pos_y, caracter,posicion_sin_usar):
        nuevo = nodoOrtogonal(pos_x, pos_y, caracter,posicion_sin_usar) 
        self.sin_usar=posicion_sin_usar
        nodo_X = self.filas.getEncabezado(pos_x)
        nodo_Y = self.columnas.getEncabezado(pos_y)
        self.primero=nuevo
        self.vacias+=1

        if nodo_X == None: 
            nodo_X = NodoCabecera(pos_x)
            self.filas.insertar(nodo_X)

        if nodo_Y == None: 
            nodo_Y = NodoCabecera(pos_y)
            self.columnas.insertar(nodo_Y)

        # ----- INSERTAR NUEVO EN FILA
        if nodo_X.Columna == None: 
            nodo_X.Columna = nuevo
        else: 
                
            if nuevo.y < nodo_X.Columna.y: 
                nuevo.derecho = nodo_X.Columna              
                nodo_X.Columna.izquierdo = nuevo
                nodo_X.Columna = nuevo
            else:
                tmp : nodoOrtogonal = nodo_X.Columna     
                while tmp != None:                      
                    if nuevo.y < tmp.y:
                        nuevo.derecho = tmp
                        nuevo.izquierdo = tmp.izquierdo
                        tmp.izquierdo.derecha = nuevo
                        tmp.izquierdo = nuevo
                        break;
                    elif nuevo.x == tmp.x and nuevo.y == tmp.y:
                        break;
                    else:
                        if tmp.derecho == None:
                            tmp.derecho = nuevo
                            nuevo.izquierdo = tmp
                            break;
                        else:
                            tmp = tmp.derecho 
                    
        if nodo_Y.Columna == None: 
            nodo_Y.Columna = nuevo
        else: 
            if nuevo.x < nodo_Y.Columna.x:
                nuevo.abajo = nodo_Y.Columna
                nodo_Y.Columna.arriba = nuevo
                nodo_Y.Columna = nuevo
            else:
                tmp2 : nodoOrtogonal = nodo_Y.Columna
                while tmp2 != None:
                    if nuevo.x < tmp2.x:
                        nuevo.abajo = tmp2
                        nuevo.arriba = tmp2.arriba
                        tmp2.arriba.abajo = nuevo
                        tmp2.arriba = nuevo
                        break;
                    elif nuevo.x == tmp2.x and nuevo.y == tmp2.y: 
                        break;
                    else:
                        if tmp2.abajo == None:
                            tmp2.abajo = nuevo
                            nuevo.arriba = tmp2
                            break
                        else:
                            tmp2 = tmp2.abajo
    '''def Llenar(self,dimensionx,dimensiony,dato,usar):
        for i in range(int(dimensionx)):
            for j in range(int(dimensionx)):

                nuevo = nodoOrtogonal(i, j, dato,usar) 
                nodo_X = self.filas.getEncabezado(i)
                nodo_Y=self.columnas.getEncabezado(j)
                if nodo_X == None: 
                    
                    nodo_X = NodoCabecera(i)
                    self.filas.insertar(nodo_X)
                 
                if nodo_Y == None : 
                    nodo_Y = NodoCabecera(j)
                    self.columnas.insertar(nodo_Y)

                    


                if nodo_X.Columna == None: 
                    nodo_X.Columna = nuevo
                else: 
                        
                    if nuevo.y < nodo_X.Columna.y: 
                        nuevo.derecho = nodo_X.Columna              
                        nodo_X.Columna.izquierdo = nuevo
                        nodo_X.Columna = nuevo
                    else:
                        tmp : nodoOrtogonal = nodo_X.Columna     
                        while tmp != None:                      
                            if nuevo.y < tmp.y:
                                nuevo.derecho = tmp
                                nuevo.izquierdo = tmp.izquierdo
                                tmp.izquierdo.derecha = nuevo
                                tmp.izquierdo = nuevo
                                break;
                            elif nuevo.x == tmp.x and nuevo.y == tmp.y:
                                break;
                            else:
                                if tmp.derecho == None:
                                    tmp.derecho = nuevo
                                    nuevo.izquierdo = tmp
                                    break;
                                else:
                                    tmp = tmp.derecho 
                if nodo_Y.Columna == None: 
                    nodo_Y.Columna = nuevo
                else: 
                    if nuevo.x < nodo_Y.Columna.x:
                        nuevo.abajo = nodo_Y.Columna
                        nodo_Y.Columna.arriba = nuevo
                        nodo_Y.Columna = nuevo
                    else:
                        tmp2 : nodoOrtogonal = nodo_Y.Columna
                        while tmp2 != None:
                            if nuevo.x < tmp2.x:
                                nuevo.abajo = tmp2
                                nuevo.arriba = tmp2.arriba
                                tmp2.arriba.abajo = nuevo
                                tmp2.arriba = nuevo
                                break;
                            elif nuevo.x == tmp2.x and nuevo.y == tmp2.y: 
                                break;
                            else:
                                if tmp2.abajo == None:
                                    tmp2.abajo = nuevo
                                    nuevo.arriba = tmp2
                                    break
                                else:
                                    tmp2 = tmp2.abajo'''



    def get_posicion(self, posicionx, posiciony):
        posicion = self.columnas.primero
        while posicion is not None:
            if posicionx == posicion.x and posiciony == posicion.x:
                return posicion
            posicion = posicion.siguiente
        return None

    def recorrido(self):
        temporal = self.columnas.primero
        contador = 0
        while temporal is not None:
            if not (temporal.dato):
                contador += 1
            temporal = temporal.derecho
        if contador == self.vacias:
            return False
        else: 
            return True




    def graficarDibujo(self, nombre):
        contenido = '''digraph G{
    node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
    edge[style = "bold"]
    node[label = "capa:''' + str(self.size) +'''" fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        contenido += '''label = "{}" \nfontname="Arial Black" \nfontsize="25pt" \n
                    \n'''.format('\nTEJIDO')

        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="azure3" pos="-1,-{}!" shape=box]x{};'.format(pivote.x, 
            posx, pivote.x)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.x, pivote.siguiente.x)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.x, pivote.siguiente.x)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.x)

        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="azure3" pos = "{},1!" shape=box]y{};'.format(pivotey.x, 
            posy, pivotey.x)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.x, pivotey.siguiente.x)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.x, pivotey.siguiente.x)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.x)

        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : nodoOrtogonal = pivote.Columna
            while pivote_celda != None:
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.x == pivote_celda.y: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.dato == '|1|':
                    contenido += '\n\tnode[label="*" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( 
                        posy_celda, posx, pivote_celda.x, pivote_celda.y
                    )
                else:
                    contenido += '\n\tnode[label=" " fillcolor="white" pos="{},-{}!" shape=box]i{}_{};'.format( 
                        posy_celda, posx, pivote_celda.x, pivote_celda.y
                    ) 
                pivote_celda = pivote_celda.derecho
            
            pivote_celda = pivote.Columna
            while pivote_celda != None:
                if pivote_celda.derecho != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.x, pivote_celda.y,
                    pivote_celda.derecho.x, pivote_celda.derecho.y)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.x, pivote_celda.y,
                    pivote_celda.derecho.x, pivote_celda.derecho.y)
                pivote_celda = pivote_celda.derecho
        
            contenido += '\n\tx{}->i{}_{};'.format(pivote.x, pivote.Columna.x, pivote.Columna.y)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.x, pivote.Columna.x, pivote.Columna.y)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : nodoOrtogonal = pivote.Columna
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.x, pivote_celda.y,
                    pivote_celda.abajo.x, pivote_celda.abajo.y)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.x, pivote_celda.y,
                    pivote_celda.abajo.x, pivote_celda.abajo.y) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.x, pivote.Columna.x, pivote.Columna.y)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.x, pivote.Columna.x, pivote.Columna.y)
            pivote = pivote.siguiente
                
        contenido += '\n}'
        dot = "matriz_{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "matriz_{}.pdf".format(nombre)
        os.system("neato -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)