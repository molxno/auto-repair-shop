# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: vehicle.py
# Descripción: Modelo para representar un vehículo.
# =============================================================
from double_list import DoubleList
import re


class Vehicle:
    """
    Modelo para representar un vehículo.
    Permite almacenar información relevante sobre el propietario, placa, marca, modelo, año y servicios realizados.
    """

    def __init__(self, client, plate, brand, model, year):
        """
        Inicializa un vehículo con cliente, placa, marca, modelo, año y lista de servicios.
        Entradas: client (objeto Client), plate (str), brand (str), model (str), year (int)
        Salidas: Ninguna
        Pertinencia: Permite crear objetos vehículo completos para ser gestionados en la lista doble y asociados a clientes.
        """
        if not re.match(r"^[A-Z]{3}-\d{3}$", plate.upper()):
            raise ValueError(f"Formato de placa inválido: {plate}")
        if client is None:
            raise ValueError("El vehículo debe estar asociado a un cliente.")

        self.__client = client
        self.__plate = plate
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__services = DoubleList()

    @property
    def client(self):
        """
        Obtiene el cliente propietario del vehículo.
        Entradas: Ninguna
        Salidas: objeto Client
        Pertinencia: Permite acceder al propietario para reportes y validaciones.
        """
        return self.__client

    @client.setter
    def client(self, value):
        """
        Establece el cliente propietario del vehículo.
        Entradas: value (objeto Client)
        Salidas: Ninguna
        Pertinencia: Permite modificar el propietario del vehículo.
        """
        self.__client = value

    @property
    def plate(self):
        """
        Obtiene la placa del vehículo.
        Entradas: Ninguna
        Salidas: str (placa)
        Pertinencia: Permite identificar el vehículo de forma única en el sistema.
        """
        return self.__plate

    @plate.setter
    def plate(self, value):
        """
        Establece la placa del vehículo.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar la identificación única del vehículo.
        """
        self.__plate = value

    @property
    def brand(self):
        """
        Obtiene la marca del vehículo.
        Entradas: Ninguna
        Salidas: str (marca)
        Pertinencia: Permite acceder a la marca para reportes y validaciones.
        """
        return self.__brand

    @brand.setter
    def brand(self, value):
        """
        Establece la marca del vehículo.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar la marca registrada del vehículo.
        """
        self.__brand = value

    @property
    def model(self):
        """
        Obtiene el modelo del vehículo.
        Entradas: Ninguna
        Salidas: str (modelo)
        Pertinencia: Permite acceder al modelo para reportes y validaciones.
        """
        return self.__model

    @model.setter
    def model(self, value):
        """
        Establece el modelo del vehículo.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar el modelo registrado del vehículo.
        """
        self.__model = value

    @property
    def year(self):
        """
        Obtiene el año del vehículo.
        Entradas: Ninguna
        Salidas: int (año)
        Pertinencia: Permite acceder al año para reportes y validaciones.
        """
        return self.__year

    @year.setter
    def year(self, value):
        """
        Establece el año del vehículo.
        Entradas: value (int)
        Salidas: Ninguna
        Pertinencia: Permite modificar el año registrado del vehículo.
        """
        self.__year = value

    @property
    def services(self):
        """
        Obtiene la lista doble de servicios realizados al vehículo.
        Entradas: Ninguna
        Salidas: DoubleList (lista de servicios)
        Pertinencia: Permite acceder y gestionar los servicios asociados al vehículo.
        """
        return self.__services

    def add_service(self, service):
        """
        Agrega un servicio a la lista de servicios del vehículo.
        Entradas: service (objeto Service)
        Salidas: Ninguna
        Pertinencia: Permite asociar servicios realizados al vehículo, cumpliendo la relación entre objetos.
        """
        self.__services.add_first(service)

    def __str__(self):
        """
        Representación en texto del vehículo.
        Entradas: Ninguna
        Salidas: str (información resumida del vehículo)
        Pertinencia: Facilita la visualización y exportación de datos del vehículo.
        """
        return f"{self.__plate} - {self.__brand} {self.__model} ({self.__year})"
