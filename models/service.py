class Service:
    def __init__(self, type_service, price, date, description):
        self.__type_service = type_service
        self.__price = price
        self.__date = date
        self.__description = description

    @property
    def type_service(self):
        return self.__type_service

    @type_service.setter
    def type_service(self, value):
        self.__type_service = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("El costo debe ser positivo.")
        self.__price = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def __str__(self):
        return f"{self.__type_service} - ${self.__price:.2f} ({self.__date})"
