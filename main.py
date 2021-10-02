import pymysql
import pymysql.cursors

class  DataBase(object):
	"""docstring for  DataBase"""
	def __init__(self):
		self.connection = pymysql.connect(
			host='localhost',
			user='root',
			password='',
			db='demo'
			)
		self.cursor = self.connection.cursor()
		print("---------------------------------------------------------")
		print("Conexion con la Base de Datos establecida existosamente")
		print("---------------------------------------------------------")
		print()
	def select_user(self, id): #Mostramos una sola fila de la base de datos
		sql = 'SELECT id, username, email FROM users WHERE id = {}'.format(id)

		try:
			self.cursor.execute(sql)
			user = self.cursor.fetchone()

			print("Id: ", user[0])
			print("Username: ", user[1])
			print("Email: ", user[2])

		except Exception as e:
			raise
	

	def select_all_user(self):  #Mostramos todas las filas de la base de datos
		sql = 'SELECT id, username, email FROM users'
		try:
			self.cursor.execute(sql)
			users = self.cursor.fetchall()

			for user in users:
				print("Id: ", user[0])
				print("Username: ", user[1])
				print("Email: ", user[2])
				print("_____\n")

		except Exception as e:
			raise e



	def update(self, username,  id):

		sql = "UPDATE  users SET username ='{}' WHERE id = {}".format(username, id) #utilizamos la funcion update para actualizar un registro de la base de datos

		try:
			self.cursor.execute(sql)

		except Exception as e:
			raise e


	def insert_new_user(self,nombre,email):
		print(nombre)
		print(email)		
		sql = "INSERT INTO users(username, email) VALUES ('{}','{}')".format(nombre,email)
		try:
			self.cursor.execute(sql)
			
			
		except Exception as e:
			raise e




database= DataBase()
#database.select_user(1)
#database.update('Cambio de nombre', 1)
#database.select_user(1)
#database.insert_new_user()
opcion=int(input("1.Cargar Nuevo Usuario , 2.Salir :  "))
print()
if opcion == 1:
	for a in range(1,2):
		nomb=input("Ingresa tu Nombre de Usuario: ")
		em= input("\n Ingresa tu email: ")
		database.insert_new_user(nomb,em)

	database.connection.commit()
else:
	print("Saliste del Programa")

#database.select_all_user()

