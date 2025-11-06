from double_list import DoubleList
import re


class Vehicle:
    def __init__(self, client, plate, brand, model, year):
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
        return self.__client

    @client.setter
    def client(self, value):
        self.__client = value

    @property
    def plate(self):
        return self.__plate

    @plate.setter
    def plate(self, value):
        self.__plate = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def services(self):
        return self.__services

    def add_service(self, service):
        self.__services.add_first(service)

    def __str__(self):
        return f"{self.__plate} - {self.__brand} {self.__model} ({self.__year})"
