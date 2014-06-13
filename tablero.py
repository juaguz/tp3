from constantes import *
from interfaz import Interfaz
from paises import *

class Tablero(object):
    """Clase que representa el tablero de juego."""

    def __init__(self, continentes, limitrofes):
        """Crea un tablero desde un diccionario de continentes con su
        lista de paises, y un diccionario de paises y su lista de
        limitrofes."""
        self.continentes = continentes
        self.limitrofes  = limitrofes
        self.paises      = {}


    def ocupar_pais(self, pais, color, ejercitos=1):
        """Ocupa el pais indicado con ejercitos del color."""
        self.paises[pais] = [color,ejercitos]
        #print(self.paises[pais])
        #return self.paises
        #raise NotImplementedError()


    def asignar_ejercitos(self, pais, ejercitos):
        """Suma o resta una cantidad de ejercitos en el pais indicado."""

        self.paises[pais][1] += ejercitos


    def actualizar_interfaz(self, agregados=None):
        """Redibuja interfaz grafica. Puede recibir un diccionario de
        paises y numero de ejercitos que se adicionan o sustraen a los
        que estan ubicados en el tablero.
        Por ejemplo, si el diccionario fuera
        {'Argentina': -1, 'Brasil': 1}, el tablero se dibujaria con un
        ejercito menos en Argentina y uno mas en Brasil."""


        Interfaz.ubicar_ejercitos(agregados)
        #raise NotImplementedError()

    # Utilizar la funcion de la Interfaz, que recibe un diccionario
    # de paises y colores, por ejemplo:
    # >>> paises = {'Argentina': (COLOR_NEGRO, 10), 'Brasil':
    # ...	(COLOR_ROSA, 1)}
    # >>> Interfaz.ubicar_ejercitos(paises)
    # Va a poner 10 ejercitos negros en Argentina y 1 rosa en
    # Brasil.


    def color_pais(self, pais):
        """Devuelve el col or de un pais."""

        return self.paises[pais][0]


    def ejercitos_pais(self, pais):
        """Devuelve la cantidad ejercitos en un pais."""
        return self.paises[pais][1]

    def es_limitrofe(self, pais1, pais2):
        """Informa si dos paises son limitrofes."""
        if pais2 in paises_limitrofes[pais1]:
            return True
        return False

    def cantidad_paises(self):
        """Informa la cantidad de paises totales."""
        #raise NotImplementedError()
        cantidad = 0
        for key in self.continentes:
            cantidad+=self.cantidad_paises_continente(self.continentes[key])
        return  cantidad

    def cantidad_paises_continente(self, continente):
        """Informa la cantidad de paises en continente."""
        return len(continente)

    def continente_pais(self, pais):
        """Informa el continente de un pais."""
        for key in self.continentes:
            if pais in self.continentes[key]:
                return key



    def paises_color(self, color):
        """Devuelve la lista de paises con ejercitos del color."""
        lista_color  = []
        for pais in self.paises:
            if pais[0] == color:
                lista_color.append(pais)
        return lista_color
