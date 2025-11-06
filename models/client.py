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
    """
    Modelo para representar un cliente del sistema.
    Hereda de Person y agrega información de contacto y vehículos asociados.
    """

    def __init__(self, name, document, phone, email, address):
        """
        Inicializa un cliente con sus datos personales, correo, dirección y lista de vehículos.
        Entradas: name (str), document (str), phone (str), email (str), address (str)
        Salidas: Ninguna
        Pertinencia: Permite crear objetos cliente completos para ser gestionados en la lista doble.
        """
        super().__init__(name, document, phone)
        self.__email = email
        self.__address = address
        self.__vehicles = DoubleList()

    @property
    def email(self):
        """
        Obtiene el correo electrónico del cliente.
        Entradas: Ninguna
        Salidas: str (correo electrónico)
        Pertinencia: Permite acceder al dato de contacto para reportes y validaciones.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Establece el correo electrónico del cliente.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar el dato de contacto del cliente.
        """
        self.__email = value

    @property
    def address(self):
        """
        Obtiene la dirección del cliente.
        Entradas: Ninguna
        Salidas: str (dirección)
        Pertinencia: Permite acceder al dato de ubicación para reportes y validaciones.
        """
        return self.__address

    @address.setter
    def address(self, value):
        """
        Establece la dirección del cliente.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar el dato de ubicación del cliente.
        """
        self.__address = value

    @property
    def vehicles(self):
        """
        Obtiene la lista doble de vehículos asociados al cliente.
        Entradas: Ninguna
        Salidas: DoubleList (lista de vehículos)
        Pertinencia: Permite acceder y gestionar los vehículos de cada cliente.
        """
        return self.__vehicles

    def add_vehicle(self, vehicle):
        """
        Agrega un vehículo a la lista de vehículos del cliente.
        Entradas: vehicle (objeto Vehicle)
        Salidas: Ninguna
        Pertinencia: Permite asociar vehículos a clientes, cumpliendo la relación entre objetos.
        """
        self.__vehicles.add_first(vehicle)

    def __str__(self):
        """
        Representación en texto del cliente.
        Entradas: Ninguna
        Salidas: str (información resumida del cliente)
        Pertinencia: Facilita la visualización y exportación de datos del cliente.
        """
        return f"Cliente: {self.name} | Correo: {self.email} | Documento: {self.document}"
