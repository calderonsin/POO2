class Usuario:
	usuarios = [] #Lista de todos los usuarios registrados

	#Constructor
	def __init__(self, usuario, correo, contrasena):
		self._usuario = usuario
		self._correo = correo
		self._contrasena = contrasena
		Usuario.usuarios.append(self)

	#Getters and Setters
	def setUsuario(self, usuario):
		self._usuario = usuario

	def setCorreo(self, correo):
		self._correo = correo

	def setContrasena(self, contrasena):
		self._contrasena = contrasena

	def getUsuario(self):
		return self._usuario

	def getCorreo(self):
		return self._correo

	def getContrasena(self):
		return self._contrasena

	