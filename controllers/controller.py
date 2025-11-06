# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: controller.py
# Descripción: Clase base abstracta para controladores de listas dobles.
# =============================================================
from abc import ABC, abstractmethod
from double_list import DoubleList


class Controller(ABC):
    """
    Clase base abstracta para controladores de listas dobles.
    Permite gestionar listas de objetos no primitivos mediante operaciones de inserción, búsqueda, eliminación y ordenamiento.
    """

    def __init__(self):
        """
        Inicializa la lista doblemente enlazada para almacenar los objetos.
        Entradas: Ninguna
        Salidas: Ninguna
        Pertinencia: Permite crear la estructura base para almacenar los elementos gestionados por el controlador.
        """
        self._items = DoubleList()

    @abstractmethod
    def get_key(self, obj):
        """
        Define el atributo clave de búsqueda para los objetos gestionados.
        Entradas: obj (objeto a buscar)
        Salidas: valor de la clave (str/int/obj)
        Pertinencia: Permite identificar de forma única cada elemento en la lista para operaciones de búsqueda y eliminación.
        """
        pass

    @abstractmethod
    def order_key(self, obj):
        """
        Define el atributo usado para ordenar los objetos en la lista.
        Entradas: obj (objeto a ordenar)
        Salidas: valor de la clave de orden (str/int/obj)
        Pertinencia: Permite mantener la lista ordenada según un criterio relevante para la solución.
        """
        pass

    def is_empty(self):
        """
        Verifica si la lista está vacía.
        Entradas: Ninguna
        Salidas: bool (True si está vacía, False si no)
        Pertinencia: Permite validar el estado de la estructura antes de realizar operaciones.
        """
        return self._items.is_empty()

    def first(self):
        """
        Devuelve el primer elemento de la lista o None si está vacía.
        Entradas: Ninguna
        Salidas: objeto almacenado o None
        Pertinencia: Permite acceder al primer elemento para recorridos o validaciones.
        """
        node = self._items.first()
        return node.data if node else None

    def all(self):
        """
        Iterador sobre todos los elementos almacenados en la lista.
        Entradas: Ninguna
        Salidas: iterador de objetos
        Pertinencia: Permite recorrer la lista para mostrar, exportar o procesar los datos.
        """
        current = self._items.first()
        while current:
            yield current.data
            current = current.next

    def add(self, obj):
        """
        Agrega un objeto a la lista manteniendo el orden definido por order_key().
        Entradas: obj (objeto a agregar)
        Salidas: Ninguna
        Pertinencia: Permite insertar nuevos elementos en la estructura de forma ordenada, facilitando búsquedas y reportes.
        """
        # Si la lista está vacía, simplemente lo inserta al inicio
        if self._items.is_empty():
            self._items.add_first(obj)
            return

        # Inserta en posición ordenada
        self._insert_ordered(obj)

    def _insert_ordered(self, obj):
        """
        Inserta un elemento manteniendo el orden definido por order_key().
        Entradas: obj (objeto a agregar)
        Salidas: Ninguna
        Pertinencia: Garantiza que la lista se mantenga ordenada según el criterio definido, optimizando búsquedas y reportes.
        """
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
        """
        Busca un elemento en la lista con base en una clave.
        Entradas: key (valor de la clave de búsqueda)
        Salidas: nodo que contiene el objeto o None
        Pertinencia: Permite localizar elementos específicos para operaciones de consulta, edición o eliminación.
        """
        current = self._items.first()
        while current is not None:
            if self.get_key(current.data) == key:
                return current
            current = current.next
        return None

    def delete(self, key):
        """
        Elimina un objeto de la lista según su clave.
        Entradas: key (valor de la clave de búsqueda)
        Salidas: bool (True si se eliminó, False si no se encontró)
        Pertinencia: Permite mantener la integridad de la estructura eliminando elementos que ya no son necesarios.
        """
        node = self.get(key)
        if node:
            self._items.remove(node)
            return True
        return False

    def display_all(self):
        """
        Muestra todos los elementos de la lista por consola.
        Entradas: Ninguna
        Salidas: Ninguna
        Pertinencia: Útil para depuración y generación de reportes visuales.
        """
        current = self._items.first()
        while current:
            print(current.data)
            current = current.next

    def order(self, reverse=False):
        """
        Ordena la lista actual según la clave definida en order_key().
        Entradas: reverse (bool, True para orden descendente)
        Salidas: Ninguna
        Pertinencia: Permite reorganizar la lista para reportes o búsquedas específicas.
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
        """
        Iterador sobre los elementos de la lista en orden.
        Entradas: Ninguna
        Salidas: iterador de objetos
        Pertinencia: Permite recorrer la lista para procesar o exportar los datos.
        """
        current = self._items.first()
        while current:
            yield current.data
            current = current.next

    def __iter__(self):
        """
        Permite que el controlador sea iterable.
        Entradas: Ninguna
        Salidas: iterador de objetos
        Pertinencia: Facilita el uso de bucles for y otras operaciones de recorrido sobre la lista.
        """
        return self.iterate()
