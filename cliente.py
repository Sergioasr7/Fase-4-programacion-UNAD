import re
from entidad import Entidad
from excepciones import ClienteInvalidoError


class Cliente(Entidad):

    def __init__(self, nombre, correo):
        self.set_nombre(nombre)
        self.set_correo(correo)

    # Encapsulación
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ClienteInvalidoError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, correo):
            raise ClienteInvalidoError("Correo inválido.")

        self.__correo = correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} | Correo: {self.__correo}"
