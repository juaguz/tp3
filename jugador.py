from interfaz import Interfaz
from constantes import *
from paises import *


class Jugador(object):
    """Representa a un jugador de TEG."""

    def __init__(self, color, nombre):
        """Crea un jugador desde un color y un nombre."""
        self.color = color
        self.nombre = nombre


    def atacar(self, tablero):
        """Le pide al usuario que ingrese un par de paises para
        realizar un ataque. Devuelve None si el jugador no quiere
        atacar y un par (atacante, atacado) en caso contrario."""
        while True:
            Interfaz.setear_titulo('%s ataca. Seleccionar atacante' % self)

            atacante, boton = Interfaz.seleccionar_pais()
            while boton == Interfaz.BOTON_IZQUIERDO and (
                    tablero.color_pais(atacante) != self.color or tablero.ejercitos_pais(atacante) == 1):
                atacante, boton = Interfaz.seleccionar_pais()
            if boton != Interfaz.BOTON_IZQUIERDO:
                return None

            Interfaz.setear_titulo('%s ataca. Seleccionar pais atacado por %s' % (self, atacante))

            atacado, boton = Interfaz.seleccionar_pais()
            while boton == Interfaz.BOTON_IZQUIERDO and (
                    tablero.color_pais(atacado) == self.color or not tablero.es_limitrofe(atacante, atacado)):
                atacado, boton = Interfaz.seleccionar_pais()
            if boton != Interfaz.BOTON_IZQUIERDO:
                continue

            return (atacante, atacado)

    def agregar_ejercitos(self, tablero, cantidad):
        """Recibe un tablerox y un diccionario con la cantidad de paises
        a poner. Devuelve un diccionario con los paises que el usuario
        selecciono.
        Por ejemplo, si cantidad = {"": 2, "Africa": 3}, eso significa
        que el jugador va a poner 5 ejercitos en sus paises, de los
        cuales 7 tienen que estar obligatoriamente en Asia.
        Un ejemplo de retorno de la funcion podria ser
        {"Zaire": 4, "Italia": 1}."""
        #return {"Zaire": 4, "Italia": 1}
        self.ejercitos_paises = {}

        paises = dar_paises()
        ejercitos_paises = {}
        opciones_paises = []
        for pais in paises:
            if tablero.color_pais(pais) == self.color:
               opciones_paises.append(pais)
        for key in cantidad:
            opciones_paises_aux = []
            for i in range(0,cantidad[key]):
                if len(key) == 0:
                    self.sumar_ejercito(opciones_paises)
                else:
                    for pais in opciones_paises:
                        if pais in paises_por_continente[key]:
                            opciones_paises_aux.append(pais)
                    self.sumar_ejercito(opciones_paises_aux)

        return  self.ejercitos_paises











    def sumar_ejercito(self,opciones_paises):
        pais = Interfaz.elegir('Agregar Ejercito','Seleccione el pais, para agregar tropas',opciones_paises)
        if self.ejercitos_paises.has_key(pais):
            self.ejercitos_paises[pais]+=1
        else:
            self.ejercitos_paises[pais]=1


    def reagrupar(self, tablero):
        """Recibe el tablero y le pide al jugador que seleccione todos
        los ejercitos que desea reagrupar. Devuelve una lista de
        reagrupamientos.
        Solo se podran reagrupar ejercitos a paises limitrofes, nunca
        un pais podra quedar vacio.
        Un ejemplo de devolcion de esta funcion puede ser:
        [('Argentina', 'Uruguay', 2), ('Argentina', 'Brasil', 1),
            ('Chile', 'Argentina', 1)]
        Esto significa que de Argentina se reagrupan 3 ejercitos, 2 con
        destino a Uruguay y 1 con destino a Brasil. Argentina tiene que
        tener al menos 4 ejercitos. De Chile se pasa uno a Argentina,
        por lo que Chile tiene que tener al menos 1. Todos los paises
        tienen que pertenecer al jugador. Despues de implementado el
        reagrupamiento, Brasil quedara con 1 ejercito mas, Uruguay con
        2 mas, Argentina con 2 menos (salen 3, entra 1) y Chile con 1
        menos."""
        paises                  = dar_paises()
        opciones_paises         = []
        opciones_paises_destino = []
        lista_reagrupamientos   = []

        for pais in paises:
            if (tablero.paises[pais][0] == self.color) and (tablero.paises[pais][1] > 1):
                opciones_paises.append(pais)

        pais_origen        = Interfaz.elegir('Reagrupar Ejercitos','Seleccione el pais de origen',opciones_paises)
        opciones_paises.remove(pais_origen)
        cantidad_ejercitos = tablero.paises[pais_origen][1]

        for pais in  paises_limitrofes[pais_origen]:
            if tablero.color_pais(pais) ==self.color:
                opciones_paises_destino.append(pais)

        while cantidad_ejercitos > 1:

            pais_destino              = Interfaz.elegir('Reagrupar Ejercitos','Seleccione el pais de Destino',opciones_paises_destino)
            cantidad_ejercitos_mover  = Interfaz.elegir('Reagrupar Ejercitos','Seleccione la cantidad',range(1,cantidad_ejercitos))
            cantidad_ejercitos       -= int(cantidad_ejercitos_mover)
            lista_reagrupamientos.append((pais_origen,pais_destino,cantidad_ejercitos_mover))

        return lista_reagrupamientos




    def __str__(self):
        """Representacion de un jugador."""
        return '%s (%s)' % (self.nombre, NOMBRE_COLORES[self.color])
