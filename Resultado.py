class Resultado:

	#Constructor
	def __init__(self, marca, puesto_en_categoria, premio, foto, foto2):
		self._marca = marca
		self._puesto_en_categoria  = puesto_en_categoria
		self._premio = premio
		self._foto = False
		self._foto2 = False

	#Getters and Setters
	def setMarca(self, marca):
		self.marca = marca

	def setPuesto_en_categoria(self, puesto_en_categoria):
		self._puesto_en_categoria = puesto_en_categoria

	def setPremio(self, premio):
		self._premio = premio

	def setFoto(self, foto):
		self._foto = foto

	def setFoto2(self, foto2):
		self._foto2 = foto2

	def getMarca(self):
		return self._marca

	def getPuesto_en_categoria(self):
		return self._puesto_en_categoria

	def getPremio(self):
		return self._premio

	def getFoto(self):
		return self._foto

	def getFoto2(self):
		return self._foto2

	def get()
