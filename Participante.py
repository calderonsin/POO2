from Usuario import Usuario

class Participante(Usuario):

	#Constructor
	def __init__(self, usuario, correo, contrasena, nombres, apellidos, documento, fecha_de_nacimiento, genero, eps, pais, rh):
		super().__init__(self, usuario, correo, contraseña)
		self._nombres = nombres
		self._apellidos = apellidos
		self._documento = documento
		self._fecha_de_nacimiento = fecha_de_nacimiento
		self._genero = genero
		self._eps = eps
		self._pais = pais
		self._rh = rh


	#Geterrs and Setters

	def setNombres(self, nombres):
		self._nombres = nombres

	def setApellidos(self, apellidos):
		self._apellidos = apellidos

	def setDocumento(self, documento):
		self._documento = documento

	def setFecha_de_nacimiento(self, fecha_de_nacimiento):
		self._fecha_de_nacimiento = fecha_de_nacimiento

	def setGenero(self, genero):
		self._genero = genero

	def setEps(self, eps):
		self._eps = eps

	def setPais(self, pais):
		self._genero = genero

	def setRh(self, rh):
		self._rh = rh

	def getNombres(self):
		return self._nombres

	def getApellidos(self):
		return self._apellidos

	def getDocumento(self):
		return self._documento

	def getFecha_de_nacimiento(self):
		return self._fecha_de_nacimiento

	def getGenero(self):
		return self._genero

	def getEps(self):
		return self._eps

	def getPais(self):
		return self._pais

	def getRh(self):
		return self.rh


	















	



























