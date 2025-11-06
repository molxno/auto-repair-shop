# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: service.py
# Descripción: Modelo para representar un servicio realizado.
# =============================================================

class Service:
    """
    Modelo para representar un servicio realizado a un vehículo.
    Permite almacenar información relevante sobre el tipo, precio, fecha y descripción del servicio.
    """

    def __init__(self, type_service, price, date, description):
        """
        Inicializa un servicio con tipo, precio, fecha y descripción.
        Entradas: type_service (str), price (float), date (date), description (str)
        Salidas: Ninguna
        Pertinencia: Permite crear objetos servicio para ser gestionados en la lista doble de servicios de cada vehículo.
        """
        if price <= 0:
            raise ValueError(f"El costo del servicio debe ser positivo: {price}")

        self.__type_service = type_service
        self.__price = price
        self.__date = date
        self.__description = description

    @property
    def type_service(self):
        """
        Obtiene el tipo de servicio realizado.
        Entradas: Ninguna
        Salidas: str (tipo de servicio)
        Pertinencia: Permite identificar el tipo de trabajo realizado en el vehículo.
        """
        return self.__type_service

    @type_service.setter
    def type_service(self, value):
        """
        Establece el tipo de servicio realizado.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar el tipo de trabajo registrado.
        """
        self.__type_service = value

    @property
    def price(self):
        """
        Obtiene el precio del servicio.
        Entradas: Ninguna
        Salidas: float (precio)
        Pertinencia: Permite acceder al costo para reportes y validaciones.
        """
        return self.__price

    @price.setter
    def price(self, value):
        """
        Establece el precio del servicio.
        Entradas: value (float)
        Salidas: Ninguna
        Pertinencia: Permite modificar el costo registrado del servicio.
        """
        self.__price = value

    @property
    def date(self):
        """
        Obtiene la fecha en que se realizó el servicio.
        Entradas: Ninguna
        Salidas: date (fecha)
        Pertinencia: Permite acceder a la fecha para ordenamiento y reportes.
        """
        return self.__date

    @date.setter
    def date(self, value):
        """
        Establece la fecha del servicio.
        Entradas: value (date)
        Salidas: Ninguna
        Pertinencia: Permite modificar la fecha registrada del servicio.
        """
        self.__date = value

    @property
    def description(self):
        """
        Obtiene la descripción del servicio realizado.
        Entradas: Ninguna
        Salidas: str (descripción)
        Pertinencia: Permite acceder a detalles adicionales del trabajo realizado.
        """
        return self.__description

    @description.setter
    def description(self, value):
        """
        Establece la descripción del servicio realizado.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar los detalles adicionales del servicio.
        """
        self.__description = value

    def __str__(self):
        """
        Representación en texto del servicio.
        Entradas: Ninguna
        Salidas: str (información resumida del servicio)
        Pertinencia: Facilita la visualización y exportación de datos del servicio.
        """
        return f"{self.__type_service} - ${self.__price:.2f} ({self.__date})"
