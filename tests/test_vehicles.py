# =============================================================
# Archivo: tests/test_vehicles.py
# Descripción: Pruebas unitarias para la gestión de vehículos
# =============================================================
from controllers.client_controller import ClientController
from controllers.vehicle_controller import VehicleController
from models.client import Client
from models.vehicle import Vehicle


def test_vehicles():
    print("\n================ PRUEBAS DE VEHÍCULOS ================")
    vehicle_controller = VehicleController()
    client_controller = ClientController()

    try:
        cliente = Client("Isabella Diaz", "1025646344", "3206686822", "isa_diaza@gmail.com", "Carrera 56 #43-12")
        client_controller.add_client(cliente)

        vehiculo_valido = Vehicle(cliente, "ABC-123", "Toyota", "Corolla", 2020)
        vehicle_controller.add_vehicle(vehiculo_valido, client_controller)
        print("✅ Vehículo insertado correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar vehículo válido: {e}")

    try:
        vehiculo_placa_mal = Vehicle(cliente, "AB123", "Mazda", "3", 2021)
        vehicle_controller.add_vehicle(vehiculo_placa_mal, client_controller)
        print("❌ Vehículo con placa inválida insertado (debería fallar).")
    except Exception as e:
        print(f"✅ Error esperado por placa inválida: {e}")

    try:
        vehiculo_sin_cliente = Vehicle(None, "XYZ-789", "Renault", "Logan", 2019)
        vehicle_controller.add_vehicle(vehiculo_sin_cliente, client_controller)
        print("❌ Vehículo sin cliente insertado (debería fallar).")
    except Exception as e:
        print(f"✅ Error esperado por cliente nulo: {e}")
