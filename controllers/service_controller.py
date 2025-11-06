from controllers.controller import Controller
from models.service import Service


class ServiceController(Controller):
    """Controlador para gestionar los servicios realizados."""

    def get_key(self, service: Service):
        """Clave de búsqueda: combinación tipo-fecha."""
        return f"{service.type_service}-{service.date}"

    def order_key(self, service: Service):
        """Orden descendente por fecha."""
        return service.date

    def add_service(self, service):
        """Agrega un nuevo servicio, validando precio."""
        if service.price <= 0:
            print(f"❌ No se puede registrar servicio con costo negativo: {service.price}")
            return False
        self._insert_ordered_desc(service)
        return True

    def _insert_ordered_desc(self, obj):
        """Inserta descendente según order_key()."""
        key_obj = self.order_key(obj)
        current = self._items.first()

        while current is not None:
            key_current = self.order_key(current.data)
            # nota: invertimos la comparación
            if key_obj > key_current:
                self._items.add_before(current, obj)
                return
            current = current.next

        self._items.add_last(obj)

    def get_service(self, type_service, date):
        """Obtiene un servicio por tipo y fecha."""
        key = f"{type_service}-{date}"
        node = self.get(key)
        return node.data if node else None

    def delete_service(self, type_service, date):
        """Elimina un servicio basado en tipo y fecha."""
        key = f"{type_service}-{date}"
        return self.delete(key)
