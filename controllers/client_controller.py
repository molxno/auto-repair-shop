from controllers.controller import Controller
from models.client import Client


class ClientController(Controller):
    """Controlador para gestionar clientes y sus vehículos."""

    def get_key(self, client: Client):
        """La clave para buscar clientes es su documento."""
        return client.document

    def order_key(self, client: Client):
        """Orden alfabético por nombre."""
        return client.name.lower()

    def add_client(self, client: Client):
        """Agrega un cliente nuevo a la lista."""
        self.add(client)

    def add_vehicle_to_client(self, document, vehicle):
        """Agrega un vehículo a un cliente existente."""
        node = self.get(document)
        if node:
            node.data.add_vehicle(vehicle)
            return True
        return False

    def get_client(self, document):
        """Obtiene el objeto Client completo."""
        node = self.get(document)
        return node.data if node else None

    def delete_client(self, document):
        """Elimina un cliente solo si no tiene servicios activos."""
        node = self.get(document)
        if not node:
            return False

        client = node.data
        temp_vehicle = client.vehicles.first()
        while temp_vehicle:
            vehicle = temp_vehicle.data
            if not vehicle.services.is_empty():
                print(f"❌ No se puede eliminar al cliente {client.name}: tiene servicios activos.")
                return False
            temp_vehicle = temp_vehicle.next

        self._items.remove(node)
        return True

    def to_file(self, file_name):
        """
        Genera un archivo de texto con la información de los clientes,
        mostrando el número total de vehículos y el promedio de costo
        de los servicios de todos sus vehículos.
        """
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write("=== Reporte de Taller Mecánico ===\n\n")

                temp_client = self._items.first()
                while temp_client is not None:
                    client = temp_client.data

                    total_services_cost = 0
                    total_services_count = 0
                    vehicle_count = 0

                    temp_vehicle = client.vehicles.first()
                    while temp_vehicle is not None:
                        vehicle = temp_vehicle.data
                        vehicle_count += 1

                        temp_service = vehicle.services.first()
                        while temp_service is not None:
                            service = temp_service.data
                            total_services_cost += service.price
                            total_services_count += 1
                            temp_service = temp_service.next

                        temp_vehicle = temp_vehicle.next

                    # Calcular promedio
                    average_cost = (
                        total_services_cost / total_services_count
                        if total_services_count > 0 else 0
                    )

                    # Escribir en el archivo
                    file.write(f"Cliente: {client.name}\n")
                    file.write(f"Vehículos: {vehicle_count}\n")
                    file.write(f"Promedio de servicios: ${average_cost:,.0f}\n\n")

                    temp_client = temp_client.next

            print(f"✅ Reporte generado correctamente en '{file_name}'")

        except Exception as e:
            print(f"❌ Error al generar el reporte: {e}")
