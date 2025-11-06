# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: tests/test_cases.py
# Descripción: Casos de prueba automatizados para validar las funcionalidades
# =============================================================
from models.vehicle import Vehicle
from models.service import Service
from datetime import datetime


def test_vehicle_without_client():
    """
    Prueba la restricción de no permitir vehículos sin cliente asociado.
    Entradas: Ninguna
    Salidas: Imprime resultado del caso de prueba (éxito o error esperado)
    Pertinencia: Valida que el sistema no permita registros inválidos de vehículos.
    """
    print("🔹 Caso 1: Vehículo sin cliente asociado")
    try:
        Vehicle(None, "XYZ-789", "Mazda", "CX-5", 2022)
        print("❌ ERROR: Se permitió registrar vehículo sin cliente.")
    except Exception as e:
        print(f"✅ Correcto: No se permitió — {e}")


def test_delete_client_with_active_services(clients):
    """
    Prueba la restricción de no permitir eliminar clientes con servicios activos.
    Entradas: clients (ClientController)
    Salidas: Imprime resultado del caso de prueba (éxito o error esperado)
    Pertinencia: Valida que el sistema preserve la integridad de los datos y las relaciones.
    """
    print("\n🔹 Caso 2: Eliminar cliente con servicios activos")
    try:
        first_client = clients.first()
        first_vehicle = first_client.vehicles.first().data
        if not first_vehicle.services.is_empty():
            deleted = clients.delete_client(first_client.document)
            print("✅ Correcto: No se puede eliminar cliente con servicios activos."
                  if not deleted else "❌ ERROR: Se eliminó cliente con servicios activos.")
        else:
            print("⚠️ Cliente no tiene servicios activos, se omite prueba.")
    except Exception as e:
        print(f"✅ Correcto: Restricción aplicada — {e}")


def test_invalid_plate_format(clients):
    """
    Prueba la restricción de formato de placa inválido en vehículos.
    Entradas: clients (ClientController)
    Salidas: Imprime resultado del caso de prueba (éxito o error esperado)
    Pertinencia: Valida que el sistema rechace placas con formato incorrecto.
    """
    print("\n🔹 Caso 3: Formato inválido de placa")
    try:
        bad_plate = Vehicle(None, "12-ABC", "Toyota", "Corolla", 2023)
        first_client = clients.first()
        clients.add_vehicle_to_client(first_client.document, bad_plate)
        print("❌ ERROR: Se aceptó una placa con formato incorrecto.")
    except Exception as e:
        print(f"✅ Correcto: Placa inválida detectada — {e}")


def test_negative_service_cost(clients):
    """
    Prueba la restricción de no permitir servicios con costo negativo.
    Entradas: clients (ClientController)
    Salidas: Imprime resultado del caso de prueba (éxito o error esperado)
    Pertinencia: Valida que el sistema rechace servicios con valores inválidos.
    """
    print("\n🔹 Caso 4: Servicio con costo negativo")
    try:
        bad_service = Service("Cambio de aceite", -50000, datetime.now().date(), "Error de costo")
        first_client = clients.first()
        first_vehicle = first_client.vehicles.first().data
        first_vehicle.add_service(bad_service)
        print("❌ ERROR: Se permitió servicio con costo negativo.")
    except Exception as e:
        print(f"✅ Correcto: Costo inválido detectado — {e}")


def test_clients_sorted(clients):
    print("\n🔹 Caso 5: Orden alfabético de clientes")
    clients.display_all()
    print("✅ Verifica visualmente: los clientes deben estar ordenados alfabéticamente.\n")


def test_services_sorted_desc(services):
    print("🔹 Caso 6: Orden descendente de servicios")
    if not services.is_empty():
        print("📋 Lista de servicios (orden descendente esperado):")
        last_date = None
        correctly_sorted = True
        for service in services:
            print(service)
            if last_date and service.appointment > last_date:
                correctly_sorted = False
            last_date = service.appointment
        print("✅ Correcto: Servicios en orden descendente por fecha."
              if correctly_sorted else "❌ ERROR: Servicios no están ordenados correctamente.")
    else:
        print("⚠️ No hay servicios para probar el ordenamiento.")
