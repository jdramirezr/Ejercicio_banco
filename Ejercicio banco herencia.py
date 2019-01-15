




class cuenta():

	def __init__(self,titular,cantidad):
		self.titular=titular
		self.cantidad=cantidad

	def imprimir(self):
		print(self.titular,self.cantidad)

class plazofijo(cuenta):

	
	def __init__(self,titular,cantidad,plazo,interes):
		super().__init__(titular,cantidad)
		self.plazo=plazo
		self.interes=interes



	def obtenerimporte(self):
		self.total=((self.cantidad*self.interes)/100)
		self.mostrarlainfo()

	def mostrarlainfo(self):
		print("datos del titular ",self.titular,self.cantidad," interes: ", self.interes,
			"total interes: ",self.total)




class cajadeahorro(cuenta):
	#metodo para heredar los datos 
	
	def __init__(self,titular,cantidad):
		super().__init__(titular,cantidad)

	def mostrar_info(self):
		print(self.titular,self.cantidad)



menu=[" que tipo de cuenta tiene:",
"1. plazofijo ",
"2. caja de ahorro"]

for i in menu:
	print(i)

opcion=int(input())

if opcion ==1:

	titular=input("escriba el nombre del titular")
	cantidad=int(input("escriba la cantidad"))
	plazo=int(input("escriba el plazo en dias"))
	interes=int(input("escriba el interes"))

	cliente1=plazofijo(titular,cantidad,plazo,interes)
	cliente1.obtenerimporte()



if opcion==2:

	titular=input("escriba el nombre del titular")
	cantidad=int(input("escriba la cantidad"))

	cliente1=cajadeahorro(titular,cantidad)
	cliente1.mostrar_info()

