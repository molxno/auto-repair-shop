from controllers.controller import Controller
from models.vehicle import Vehicle
import re


class VehicleController(Controller):
    """Controlador para gestionar vehículos y sus servicios."""

    def get_key(self, vehicle: Vehicle):
        """Clave de identificación: placa."""
        return vehicle.plate

    def order_key(self, vehicle: Vehicle):
        """Orden por cantidad de servicios (mayor a menor)."""
        count = 0
        temp = vehicle.services.first()
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def __validate_plate(self, plate: str) -> bool:
        """Valida el formato de placa (3 letras + 3 números, ejemplo: ABC-123)."""
        return re.match(r"^[A-Z]{3}-\d{3}$", plate.upper()) is not None

    def add_vehicle(self, vehicle: Vehicle, client_controller):
        """Agrega un vehículo nuevo, validando cliente y formato."""
        # Validar formato de placa
        if not self.__validate_plate(vehicle.plate):
            print(f"❌ Formato de placa inválido: {vehicle.plate}")
            return False

        # Validar cliente asociado
        client = vehicle.client
        if not client_controller.get(client.document):
            print(f"❌ No se puede registrar vehículo sin cliente asociado ({vehicle.plate}).")
            return False

        # Registrar vehículo
        self.add(vehicle)
        return True

    def add_service_to_vehicle(self, plate, service):
        """Agrega un servicio a un vehiculo existente."""
        node = self.get(plate)
        if node:
            node.data.add_service(service)
            return True
        return False

    def get_vehicle(self, plate):
        """Obtiene el objeto Vehicle completo."""
        node = self.get(plate)
        return node.data if node else None

    def delete_vehicle(self, plate):
        """Elimina un vehículo según su placa."""
        return self.delete(plate)
