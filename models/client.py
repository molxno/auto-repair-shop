# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: client.py
# Descripción: Modelo para representar un cliente.
# =============================================================
from double_list import DoubleList
from models.person import Person


class Client(Person):
    def __init__(self, name, document, phone, email, address):
        super().__init__(name, document, phone)
        self.__email = email
        self.__address = address
        self.__vehicles = DoubleList()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def vehicles(self):
        return self.__vehicles

    def add_vehicle(self, vehicle):
        self.__vehicles.add_first(vehicle)

    def __str__(self):
        return f"Cliente: {self.name} | Correo: {self.email} | Documento: {self.document}"
