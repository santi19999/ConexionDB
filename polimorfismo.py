class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando 4 ruedas")
class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando 2 ruedas")
class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo):#vehiculo es la que produce el Polimorfismo
	vehiculo.desplazamiento()

miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo)