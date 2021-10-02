class Coche(object):
	"""docstring for ClassName"""

	def __init__(self):           #Creamos un constructor, que lo que hace es que cada objeto que creemos van a tener estos valores por defecto al crearlos
		self.__largoChasis=250   #Con los dos guiones estamos encapsulando la variable, no podrá ser llamada ni consultada desde fuera de la clase.
		self.__anchoChasis =120
		self.__ruedas=4
		self.__enmarcha=False 

	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos

		if self.__enmarcha:
			return "El auto está encendido"
		else:
			return "El auto está apagado"

	def estado(self):
		print("El coche tiene: ", self.__ruedas," ruedas.")
		print("Su Chasis mide: ", self.__anchoChasis,"de Ancho y ",self.__largoChasis," de largo. ")
	
	def apagar(self):
		self.__enmarcha=False


miCoche = Coche()    #Instaciar clase o crear un objeto coche

miCoche.estado()

miCoche2 = Coche()


