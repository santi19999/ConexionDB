class Coche(object):
	"""docstring for ClassName"""

	def __init__(self):           #Creamos un constructor, que lo que hace es que cada objeto que creemos van a tener estos valores por defecto al crearlos
		self.__largoChasis=250   #Con los dos guiones estamos encapsulando la variable, no podrá ser llamada ni consultada desde fuera de la clase.
		self.__anchoChasis =120
		self.__ruedas=4
		self.__enmarcha=False 

	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos

		if(self.__enmarcha):
			chequeo=self.__chequeo_interno()


		if (self.__enmarcha and chequeo):
			print("-------------------------------------")
			print("Chequeo Correcto, puede arrancar")
			print("-------------------------------------"+"\n")

			return "El auto está encendido"

		elif(self.__enmarcha and chequeo==False):
			return "Ocurrió algo mal en el chequeo interno, no podemos arrancar! "
		
		else:
			return "El auto está apagado"

	def estado(self):
		print("El coche tiene: ", self.__ruedas," ruedas.")
		print("Su Chasis mide: ", self.__anchoChasis,"de Ancho y ",self.__largoChasis," de largo. " +"\n")
	
	def __chequeo_interno(self):
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
			return True
		else:
			return False
	def apagar(self):
		self.__enmarcha=False


print("-----------------Coche 1----------------------------")

miCoche = Coche()    #Instaciar clase o crear un objeto coche

print(miCoche.arrancar(True))

miCoche.estado()


print("-------------------Coche 2--------------------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()


