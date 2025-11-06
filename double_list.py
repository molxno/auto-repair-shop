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
    """Implementación de una lista doblemente enlazada."""

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return len(self) == 0

    def first(self):
        return self.__head

    def last(self):
        return self.__tail

    def add_first(self, data):
        node = DoubleNode(data)
        if self.is_empty():
            self.__head = self.__tail = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        self.__size += 1

    def add_last(self, data):
        node = DoubleNode(data)
        if self.is_empty():
            self.__head = self.__tail = node
        else:
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node
        self.__size += 1

    def remove_first(self):
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
        """Imprime los elementos de la lista en orden."""
        current = self.__head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
