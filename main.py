# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: main.py
# Descripción: Programa principal con carga de datos y pruebas
# =============================================================
from controllers.client_controller import ClientController
from controllers.vehicle_controller import VehicleController
from controllers.service_controller import ServiceController
from loaders import cargar_clientes, cargar_vehiculos, cargar_servicios
from tests.test_clients import test_clients
from tests.test_vehicles import test_vehicles
from tests.test_services import test_services

if __name__ == "__main__":
    clients = ClientController()
    vehicles = VehicleController()
    services = ServiceController()

    # Cargar datos
    cargar_clientes(clients, "data/clients.csv")
    cargar_vehiculos(vehicles, clients, "data/vehicles.csv")
    cargar_servicios(services, vehicles, "data/services.csv")

    print("\n=== 🧪 GENERACIÓN DE ARCHIVO ===\n")

    # Generación de reporte
    clients.to_file("output.txt")

    print("\n=== 🧪 EJECUTANDO CASOS DE PRUEBA ===\n")

    # Ejecutar pruebas
    test_clients()
    test_vehicles()
    test_services()

    print("\n✅ Todas las pruebas ejecutadas correctamente.\n")
