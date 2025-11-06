from abc import ABC, abstractmethod
from double_list import DoubleList


class Controller(ABC):
    """Clase base abstracta para controladores de listas dobles."""

    def __init__(self):
        self._items = DoubleList()

    @abstractmethod
    def get_key(self, obj):
        """Define el atributo clave de búsqueda."""
        pass

    @abstractmethod
    def order_key(self, obj):
        """Define el atributo usado para ordenar."""
        pass

    def is_empty(self):
        return self._items.is_empty()

    def first(self):
        """Devuelve el primer elemento (o None si está vacío)."""
        node = self._items.first()
        return node.data if node else None

    def all(self):
        """Iterador sobre todos los elementos almacenados."""
        current = self._items.first()
        while current:
            yield current.data
            current = current.next

    def add(self, obj):
        """Agrega un objeto manteniendo el orden según order_key()."""
        # Si la lista está vacía, simplemente lo inserta al inicio
        if self._items.is_empty():
            self._items.add_first(obj)
            return

        # Inserta en posición ordenada
        self._insert_ordered(obj)

    def _insert_ordered(self, obj):
        """Inserta un elemento manteniendo el orden definido por order_key()."""
        key_obj = self.order_key(obj)
        current = self._items.first()

        while current is not None:
            key_current = self.order_key(current.data)
            # Inserta antes si la clave del nuevo elemento es menor
            if key_obj < key_current:
                self._items.add_before(current, obj)
                return
            current = current.next

        # Si no se insertó antes de nadie, va al final
        self._items.add_last(obj)

    def get(self, key):
        """Busca un elemento en la lista con base en una clave."""
        current = self._items.first()
        while current is not None:
            if self.get_key(current.data) == key:
                return current
            current = current.next
        return None

    def delete(self, key):
        """Elimina un objeto según su clave."""
        node = self.get(key)
        if node:
            self._items.remove(node)
            return True
        return False

    def display_all(self):
        """Muestra todos los elementos (para depuración o reportes)."""
        current = self._items.first()
        while current:
            print(current.data)
            current = current.next

    def order(self, reverse=False):
        """
        Ordena la lista actual según la clave definida en `order_key`.
        Si reverse=True, el orden es descendente.
        """
        ordered = DoubleList()
        current = self._items.first()

        while current is not None:
            data = current.data
            if ordered.is_empty():
                ordered.add_first(data)
            else:
                temp = ordered.first()
                inserted = False
                while temp is not None:
                    a = self.order_key(data)
                    b = self.order_key(temp.data)
                    condition = a < b if not reverse else a > b
                    if condition:
                        ordered.add_before(temp, data)
                        inserted = True
                        break
                    temp = temp.next
                if not inserted:
                    ordered.add_last(data)
            current = current.next

        self._items = ordered

    def iterate(self):
        """Iterador sobre los elementos de la lista en orden."""
        current = self._items.first()
        while current:
            yield current.data
            current = current.next

    def __iter__(self):
        """Permite iterar directamente sobre el controlador con 'for ... in ...'."""
        return self.iterate()
