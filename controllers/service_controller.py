# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: service_controller.py
# Descripción: Controlador para gestionar los servicios realizados.
# =============================================================
from controllers.controller import Controller
from models.service import Service


class ServiceController(Controller):
    """
    Controlador para gestionar los servicios realizados.
    Permite administrar la lista de servicios, realizando operaciones de inserción, búsqueda y eliminación.
    """

    def get_key(self, service: Service):
        """
        Obtiene la clave única de un servicio (tipo-fecha).
        Entradas: service (objeto Service)
        Salidas: str (combinación tipo-fecha)
        Pertinencia: Permite identificar y buscar servicios de forma única en la lista.
        """
        return f"{service.type_service}-{service.date}"

    def order_key(self, service: Service):
        """
        Obtiene la clave de ordenamiento para un servicio (fecha).
        Entradas: service (objeto Service)
        Salidas: date (fecha del servicio)
        Pertinencia: Permite mantener la lista de servicios ordenada por fecha.
        """
        return service.date

    def add_service(self, service):
        """
        Agrega un nuevo servicio, validando que el precio sea positivo.
        Si el precio es inválido, lanza excepción.
        """
        if service.price <= 0:
            raise Exception(f"El costo del servicio debe ser positivo: {service.price}")
        self._insert_ordered_desc(service)
        return True

    def _insert_ordered_desc(self, obj):
        """
        Inserta un servicio en la lista de forma descendente por fecha.
        Entradas: obj (objeto Service)
        Salidas: Ninguna
        Pertinencia: Permite mantener la lista de servicios ordenada de más reciente a más antiguo.
        """
        key_obj = self.order_key(obj)
        current = self._items.first()
        while current is not None:
            key_current = self.order_key(current.data)
            if key_obj > key_current:
                self._items.add_before(current, obj)
                return
            current = current.next
        self._items.add_last(obj)

    def get_service(self, type_service, date):
        """
        Obtiene un servicio por tipo y fecha.
        Entradas: type_service (str), date (date)
        Salidas: objeto Service o None
        Pertinencia: Permite consultar servicios específicos para reportes o validaciones.
        """
        key = f"{type_service}-{date}"
        node = self.get(key)
        return node.data if node else None

    def delete_service(self, type_service, date):
        """
        Elimina un servicio basado en tipo y fecha. Si no existe, lanza una excepción.
        """
        key = f"{type_service}-{date}"
        result = self.delete(key)
        if not result:
            raise Exception(f"❌ No existe servicio {type_service} en fecha {date}")
        return result
