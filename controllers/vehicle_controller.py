# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: vehicle_controller.py
# Descripción: Controlador para gestionar vehículos y sus servicios.
# =============================================================
from controllers.controller import Controller
from models.vehicle import Vehicle
import re


class VehicleController(Controller):
    """
    Controlador para gestionar vehículos y sus servicios.
    Permite administrar la lista de vehículos, asociarlos a clientes y gestionar los servicios realizados.
    """

    def get_key(self, vehicle: Vehicle):
        """
        Obtiene la clave única de un vehículo (placa).
        Entradas: vehicle (objeto Vehicle)
        Salidas: str (placa del vehículo)
        Pertinencia: Permite identificar y buscar vehículos de forma única en la lista.
        """
        return vehicle.plate

    def order_key(self, vehicle: Vehicle):
        """
        Obtiene la clave de ordenamiento para un vehículo (cantidad de servicios).
        Entradas: vehicle (objeto Vehicle)
        Salidas: int (cantidad de servicios asociados)
        Pertinencia: Permite mantener la lista de vehículos ordenada por actividad de servicios.
        """
        count = 0
        temp = vehicle.services.first()
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def __validate_plate(self, plate: str) -> bool:
        """
        Valida el formato de placa (3 letras + 3 números, ejemplo: ABC-123).
        Entradas: plate (str, placa del vehículo)
        Salidas: bool (True si el formato es válido, False si no)
        Pertinencia: Garantiza la integridad de los datos y evita registros incorrectos.
        """
        return re.match(r"^[A-Z]{3}-\d{3}$", plate.upper()) is not None

    def add_vehicle(self, vehicle: Vehicle, client_controller):
        """
        Agrega un vehículo nuevo, validando cliente y formato de placa.
        Entradas: vehicle (objeto Vehicle), client_controller (ClientController)
        Salidas: bool (True si se agregó, False si hay error de formato o cliente)
        Pertinencia: Permite registrar vehículos correctamente asociados a clientes y con datos válidos.
        """
        if not self.__validate_plate(vehicle.plate):
            print(f"❌ Formato de placa inválido: {vehicle.plate}")
            return False
        client = vehicle.client
        if not client_controller.get(client.document):
            print(f"❌ No se puede registrar vehículo sin cliente asociado ({vehicle.plate}).")
            return False
        self.add(vehicle)
        return True

    def add_service_to_vehicle(self, plate, service):
        """
        Agrega un servicio a un vehículo existente.
        Entradas: plate (str, placa del vehículo), service (objeto Service)
        Salidas: bool (True si se agregó, False si no existe el vehículo)
        Pertinencia: Permite asociar servicios realizados a los vehículos registrados en el sistema.
        """
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
