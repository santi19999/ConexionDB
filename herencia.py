class Vehiculos(object):
	"""docstring for Vehiculos"""
	def __init__(self,marca,modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
		

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca, "\n")
		print("Modelo: ",self.modelo, "\n")
		print("En Marcha : ",self.enmarcha, "\n")
		print("Acelerando: ",self.acelera, "\n")
		print("Frena: ",self.frena, "\n")


class Moto(Vehiculos):
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca: ",self.marca, "\n")
		print("Modelo: ",self.modelo, "\n")
		print("En Marcha : ",self.enmarcha, "\n")
		print("Acelerando: ",self.acelera, "\n")
		print("Frena: ",self.frena, "\n")

class Furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado = cargar
		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"

class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):
		super().__init__(marca,modelo)

		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True




miMoto=Moto("Yamaha","YBR")
miMoto.caballito()
miMoto.estado()
print("--------------------------------------")
miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
print("--------------------------------------")
class BicicletaElectrica(VElectricos,Vehiculos):
	pass

miBici=BicicletaElectrica("Orbea", "h12412")
