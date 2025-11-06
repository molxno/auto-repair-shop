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
    """
    Modelo para representar una persona.
    Permite almacenar información básica de identificación y contacto.
    """

    def __init__(self, name, document, phone):
        """
        Inicializa una persona con nombre, documento y teléfono.
        Entradas: name (str), document (str), phone (str)
        Salidas: Ninguna
        Pertinencia: Permite crear objetos base para clientes y otras entidades relacionadas.
        """
        self.__name = name
        self.__document = document
        self.__phone = phone

    @property
    def name(self):
        """
        Obtiene el nombre de la persona.
        Entradas: Ninguna
        Salidas: str (nombre)
        Pertinencia: Permite acceder al nombre para reportes y validaciones.
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Establece el nombre de la persona.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar el nombre de la persona.
        """
        self.__name = value

    @property
    def document(self):
        """
        Obtiene el documento de la persona.
        Entradas: Ninguna
        Salidas: str (documento)
        Pertinencia: Permite acceder al documento para identificación y búsquedas.
        """
        return self.__document

    @document.setter
    def document(self, value):
        """
        Establece el documento de la persona.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar el documento de la persona.
        """
        self.__document = value

    @property
    def phone(self):
        """
        Obtiene el teléfono de la persona.
        Entradas: Ninguna
        Salidas: str (teléfono)
        Pertinencia: Permite acceder al teléfono para contacto y validaciones.
        """
        return self.__phone

    @phone.setter
    def phone(self, value):
        """
        Establece el teléfono de la persona.
        Entradas: value (str)
        Salidas: Ninguna
        Pertinencia: Permite modificar el teléfono de la persona.
        """
        self.__phone = value

    def __str__(self):
        """
        Representación en texto de la persona.
        Entradas: Ninguna
        Salidas: str (información resumida de la persona)
        Pertinencia: Facilita la visualización y exportación de datos de la persona.
        """
        return f"{self.__name} (Doc: {self.__document}, Tel: {self.__phone})"
