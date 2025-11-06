# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: double_list.py
# Descripción: Implementación de una lista doblemente enlazada.
# =============================================================
from double_node import DoubleNode


class DoubleList:
    """
    Implementación de una lista doblemente enlazada.
    Permite almacenar y gestionar nodos enlazados en ambas direcciones, facilitando operaciones eficientes de inserción, eliminación y recorrido.
    """

    def __init__(self):
        """
        Inicializa la lista doblemente enlazada vacía.
        Entradas: Ninguna
        Salidas: Ninguna
        Pertinencia: Permite crear la estructura base para almacenar nodos y gestionar datos en el sistema.
        """
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __len__(self):
        """
        Devuelve el tamaño actual de la lista.
        Entradas: Ninguna
        Salidas: int (cantidad de nodos)
        Pertinencia: Permite conocer el número de elementos almacenados para validaciones y recorridos.
        """
        return self.__size

    def is_empty(self):
        """
        Verifica si la lista está vacía.
        Entradas: Ninguna
        Salidas: bool (True si está vacía, False si no)
        Pertinencia: Permite validar el estado de la estructura antes de realizar operaciones.
        """
        return len(self) == 0

    def first(self):
        """
        Devuelve el primer nodo de la lista.
        Entradas: Ninguna
        Salidas: DoubleNode o None
        Pertinencia: Permite acceder al inicio de la lista para recorridos o inserciones.
        """
        return self.__head

    def last(self):
        """
        Devuelve el último nodo de la lista.
        Entradas: Ninguna
        Salidas: DoubleNode o None
        Pertinencia: Permite acceder al final de la lista para recorridos o inserciones.
        """
        return self.__tail

    def add_first(self, data):
        """
        Agrega un nuevo nodo al inicio de la lista.
        Entradas: data (objeto a almacenar)
        Salidas: Ninguna
        Pertinencia: Permite insertar elementos en la cabeza de la lista, útil para operaciones rápidas.
        """
        node = DoubleNode(data)
        if self.is_empty():
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        self.__size += 1

    def add_last(self, data):
        """
        Agrega un nuevo nodo al final de la lista.
        Entradas: data (objeto a almacenar)
        Salidas: Ninguna
        Pertinencia: Permite insertar elementos en la cola de la lista, útil para mantener orden.
        """
        node = DoubleNode(data)
        if self.is_empty():
            self.__head = self.__tail = node
        else:
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node
        self.__size += 1

    def remove_first(self):
        """
        Elimina y retorna el primer nodo de la lista.
        Entradas: Ninguna
        Salidas: objeto almacenado o None
        Pertinencia: Permite eliminar el elemento más antiguo o prioritario de la lista.
        """
        if self.is_empty():
            return None

        data = self.__head.data
        if len(self) == 1:
            self.__head = self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None
        self.__size -= 1
        return data

    def remove_last(self):
        """
        Elimina y retorna el último nodo de la lista.
        Entradas: Ninguna
        Salidas: objeto almacenado o None
        Pertinencia: Permite eliminar el elemento más reciente o final de la lista.
        """
        if self.is_empty():
            return None

        data = self.__tail.data
        if len(self) == 1:
            self.__head = self.__tail = None
        else:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        self.__size -= 1
        return data

    def add_after(self, node, data):
        """
        Agrega un nuevo nodo después de un nodo dado.
        Entradas: node (DoubleNode), data (objeto a almacenar)
        Salidas: Ninguna
        Pertinencia: Permite insertar elementos en posiciones específicas de la lista.
        """
        if node == self.__tail:
            self.add_last(data)
        else:
            new_node = DoubleNode(data)
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node
            self.__size += 1

    def add_before(self, node, data):
        """
        Agrega un nuevo nodo antes de un nodo dado.
        Entradas: node (DoubleNode), data (objeto a almacenar)
        Salidas: Ninguna
        Pertinencia: Permite insertar elementos en posiciones específicas de la lista.
        """
        if node == self.__head:
            self.add_first(data)
        else:
            new_node = DoubleNode(data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node
            self.__size += 1

    def remove(self, node):
        """
        Elimina y retorna un nodo específico de la lista.
        Entradas: node (DoubleNode)
        Salidas: objeto almacenado
        Pertinencia: Permite eliminar elementos en posiciones arbitrarias de la lista.
        """
        if node == self.__head:
            return self.remove_first()
        elif node == self.__tail:
            return self.remove_last()
        else:
            data = node.data
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = node.prev = None
            self.__size -= 1
            return data

    def display(self):
        """
        Imprime los elementos de la lista en orden.
        Entradas: Ninguna
        Salidas: Ninguna
        Pertinencia: Permite visualizar el contenido de la lista para depuración o reportes.
        """
        current = self.__head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
