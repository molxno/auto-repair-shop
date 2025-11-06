# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: double_node.py
# Descripción: Nodo para una lista doblemente enlazada.
# =============================================================
class DoubleNode:
    """Nodo para una lista doblemente enlazada."""

    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, node):
        self.__prev = node

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node
