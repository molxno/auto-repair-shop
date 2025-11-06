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
    """
    Nodo para una lista doblemente enlazada.
    Permite almacenar un dato y referencias al nodo anterior y siguiente.
    """

    def __init__(self, data=None):
        """
        Inicializa un nodo con el dato y referencias vacías.
        Entradas: data (objeto a almacenar, puede ser cualquier tipo)
        Salidas: Ninguna
        Pertinencia: Permite crear nodos para ser enlazados en la estructura de lista doble.
        """
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        """
        Obtiene el dato almacenado en el nodo.
        Entradas: Ninguna
        Salidas: objeto almacenado
        Pertinencia: Permite acceder al valor guardado en el nodo para operaciones de la lista.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Establece el dato almacenado en el nodo.
        Entradas: value (objeto)
        Salidas: Ninguna
        Pertinencia: Permite modificar el valor guardado en el nodo.
        """
        self.__data = value

    @property
    def prev(self):
        """
        Obtiene la referencia al nodo anterior.
        Entradas: Ninguna
        Salidas: DoubleNode o None
        Pertinencia: Permite recorrer la lista hacia atrás y realizar operaciones de enlace.
        """
        return self.__prev

    @prev.setter
    def prev(self, node):
        """
        Establece la referencia al nodo anterior.
        Entradas: node (DoubleNode o None)
        Salidas: Ninguna
        Pertinencia: Permite modificar el enlace hacia el nodo anterior en la lista.
        """
        self.__prev = node

    @property
    def next(self):
        """
        Obtiene la referencia al nodo siguiente.
        Entradas: Ninguna
        Salidas: DoubleNode o None
        Pertinencia: Permite recorrer la lista hacia adelante y realizar operaciones de enlace.
        """
        return self.__next

    @next.setter
    def next(self, node):
        """
        Establece la referencia al nodo siguiente.
        Entradas: node (DoubleNode o None)
        Salidas: Ninguna
        Pertinencia: Permite modificar el enlace hacia el nodo siguiente en la lista.
        """
        self.__next = node
