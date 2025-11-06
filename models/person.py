# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: person.py
# Descripción: Modelo para representar una persona.
# =============================================================
class Person:
    def __init__(self, name, document, phone):
        self.__name = name
        self.__document = document
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def document(self):
        return self.__document

    @document.setter
    def document(self, value):
        self.__document = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value

    def __str__(self):
        return f"{self.__name} (Doc: {self.__document}, Tel: {self.__phone})"
