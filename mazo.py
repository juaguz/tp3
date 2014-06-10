from constantes import *


class Tarjeta(object):
    """Implementacion de una tarjeta de pais."""

    def __init__(self, pais, tipo):
        """Constructor desde pais y tipo."""
        self.pais = pais
        self.tipo = tipo

    def __str__(self):
        """Representacion grafica."""
        return "(%s, %s)" % (self.pais, NOMBRE_TARJETAS[self.tipo])


class Mazo(object):
    """Implementacion del mazo de tarjetas de pais."""

    def __init__(self, paises_por_tarjeta):
        """Creacion desde un diccionario de paises segun tipo.
        Debe inicializar el mazo con todas las tarjetas mezcladas."""
        l = []
        for clave in paises_por_tarjeta:
            for elem in paises_por_tarjeta[clave]:
                l.append([clave, elem])
        self.pila = []
        self.descarte = []
        for x in range(len(l)):
            rand = random.randrange(len(l))
            self.pila.append(Tarjeta(l[rand][1], l[rand][0]))

    def sacar_tarjeta(self):
        """Saca una tarjeta del mazo.
        Si el mazo se acabara, debe mezclar y empezar a repartir desde
        las tarjetas ya devueltas."""
        tarjeta = self.pila.pop()
        if self.pila == []:
            for x in range(len(self.descarte)):
                rand = random.randrange(len(self.descarte))
                self.pila.append(self.descarte[rand])
        return tarjeta

    def devolver_tarjeta(self, tarjeta):
        """Recibe una tarjeta y la guarda en el pilon de tarjetas
        devueltas. Cuando se acaben las tarjetas del mazo, se mezclaran
        las ya devueltas."""
        self.descarte.append(tarjeta)

    def cantidad_tarjetas(self):
        """Devuelve la cantidad *total* de tarjetas (tanto en el mazo
        como devueltas)."""
        return len(self.descarte) + len(self.pila)
