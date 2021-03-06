
from constantes import *
import random

def obtener_dados(n):
	"""Devuelve una lista de n numeros aleatorios (entre 1 y 6) ordenados de mayor a menor"""
	dados = [random.randrange(1,7)]
	for x in range(n - 1):
		dado = random.randrange(1,7)
		if dado > dados[0]:
			dados.insert(0, dado)
		else:
			dados.append(dado)
	return dados	

class Dados(object):
	"""Implementa la logica de tirar los dados."""

	def __init__(self):
		"""Inicializacion del objeto."""
		self.atacado_victorias = 0
		self.atacante_victorias = 0
		self.dados_atacante = []
		self.dados_atacado = []		

	def __str__(self):
		"""Representacion de la configuracion de dados de la ultima
		tirada."""
		return '(%s) Ejercitos que perdio el atacante |(%s) Ejercitos que perdio el atacante' % (self.atacante_victorias,self.atacado_victorias )

	def lanzar_dados(self, ejercitos_atacante, ejercitos_atacado):
		"""Recibe la cantidad de ejercitos presentes en el pais
		atacante y en el pais atacado. Realiza la tirada de los dados.
		El pais que ataca tiene que tener al menos dos ejercitos.
		El pais que ataca ataca con hasta un dado menos que los
		ejercitos que posee, mientras que el pais que defiende lo
		hace hasta con tantos dados como ejercitos.
		La cantidad maxima de dados con la que un pais ataca o defiende
		es siempre 3.
		Cada jugador tira sus dados.
		Los mismos se ordenan de mayor a menor.
		Si un jugador tiro mas dados que otro, los de menor valor se
		descartan.
		Se comparan uno a uno los dados ordenados.
		Cuando el valor de un dado atacante fuera *mayor* que el del
		atacado, el atacado pierde un ejercito. Si no, el atacante lo
		pierde.
		(Leer el reglamento del juego.)"""
		if ejercitos_atacante > 3:
                	ejercitos_atacante = 3
                if ejercitos_atacado > 3:
                	ejercitos_atacado = 3
                self.atacado_victorias = 0
                self.atacante_victorias = 0
                self.dados_atacante = obtener_dados(ejercitos_atacante)
                self.dados_atacado = obtener_dados(ejercitos_atacado)
                for x in range(min(ejercitos_atacante, ejercitos_atacado)):
                	if self.dados_atacado[x] >= self.dados_atacante[x]:
                		self.atacado_victorias +=1
                	else:
                		self.atacante_victorias +=1
	def ejercitos_perdidos_atacante(self):
		"""Devuelve la cantidad de ejercitos que perdio el atacante en
		la ultima tirada de dados."""
		return self.atacado_victorias

	def ejercitos_perdidos_atacado(self):
		"""Devuelve la cantidad de ejercitos que perdio el atacado en
		la ultima tirada de dados."""
		return self.atacante_victorias

