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
# Descripción: Programa principal
# =============================================================
from controllers.client_controller import ClientController
from controllers.vehicle_controller import VehicleController
from controllers.service_controller import ServiceController
from models.client import Client
from models.vehicle import Vehicle
from models.service import Service
from datetime import datetime


def cargar_clientes(controller: ClientController, file_name: str):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            next(file)  # saltar encabezado
            for linea in file:
                datos = linea.strip().split(";")
                if len(datos) < 5:
                    continue

                name = datos[0]
                document = datos[1]
                phone = datos[2]
                email = datos[3]
                address = datos[4]

                client = Client(name, document, phone, email, address)
                controller.add_client(client)
        print(f"✅ Clientes cargados desde {file_name}")
    except Exception as error:
        print(f"❌ Error al leer {file_name}: {error}")


def cargar_vehiculos(controller: VehicleController, client_controller: ClientController, file_name: str):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            next(file)
            for linea in file:
                datos = linea.strip().split(";")
                if len(datos) < 5:
                    continue

                document = datos[0]  # documento del cliente dueño
                plate = datos[1]
                brand = datos[2]
                model = datos[3]
                year = int(datos[4])

                client = client_controller.get_client(document)
                if client:
                    vehicle = Vehicle(client, plate, brand, model, year)
                    controller.add_vehicle(vehicle, client_controller)
                    client_controller.add_vehicle_to_client(document, vehicle)
                else:
                    print(f"❌ No se encontró cliente con documento {document} para el vehículo {plate}")
        print(f"✅ Vehículos cargados desde {file_name}")
    except Exception as error:
        print(f"❌ Error al leer {file_name}: {error}")


def cargar_servicios(controller: ServiceController, vehicle_controller: VehicleController, file_name: str):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            next(file)
            for linea in file:
                datos = linea.strip().split(";")
                if len(datos) < 5:
                    continue

                plate = datos[0]
                type_service = datos[1]
                price = float(datos[2])
                date = datetime.strptime(datos[3], "%d/%m/%Y").date()
                description = datos[4]

                service = Service(type_service, price, date, description)
                controller.add_service(service)
                vehicle_controller.add_service_to_vehicle(plate, service)
        print(f"✅ Servicios cargados desde {file_name}")
    except Exception as error:
        print(f"❌ Error al leer {file_name}: {error}")


if __name__ == "__main__":
    clients = ClientController()
    vehicles = VehicleController()
    services = ServiceController()

    cargar_clientes(clients, "data/clients.csv")
    cargar_vehiculos(vehicles, clients, "data/vehicles.csv")
    cargar_servicios(services, vehicles, "data/services.csv")

    # Generar reporte
    clients.to_file("output.txt")
    print("📄 Reporte generado en output.txt")

    print("\n=== 🧪 INICIO DE CASOS DE PRUEBA ===\n")

    # 1️⃣ Intentar registrar vehículo sin cliente asociado
    print("🔹 Caso 1: Vehículo sin cliente asociado")
    try:
        vehicle_no_client = Vehicle(None, "XYZ-789", "Mazda", "CX-5", 2022)
        # no se asocia con ningún cliente
        print("❌ ERROR: Se permitió registrar vehículo sin cliente.")
    except Exception as e:
        print(f"✅ Correcto: No se permitió — {e}")

    # 2️⃣ Intentar eliminar cliente con vehículos con servicios activos
    print("\n🔹 Caso 2: Eliminar cliente con servicios activos")
    try:
        first_client = clients.first()
        first_vehicle = first_client.vehicles.first().data
        # Verificamos si tiene servicios
        if not first_vehicle.services.is_empty():
            deleted = clients.delete_client(first_client.document)
            if not deleted:
                print("✅ Correcto: No se puede eliminar cliente con servicios activos.")
            else:
                print("❌ ERROR: Se eliminó cliente con servicios activos.")
        else:
            print("⚠️ Cliente no tiene servicios activos, se omite prueba.")
    except Exception as e:
        print(f"✅ Correcto: Restricción aplicada — {e}")

    # 3️⃣ Registrar vehículo con formato de placa inválido
    print("\n🔹 Caso 3: Formato inválido de placa")
    try:
        bad_plate = Vehicle(None, "12-ABC", "Toyota", "Corolla", 2023)
        first_client = clients.first()
        clients.add_vehicle_to_client(first_client.document, bad_plate)
        print("❌ ERROR: Se aceptó una placa con formato incorrecto.")
    except Exception as e:
        print(f"✅ Correcto: Placa inválida detectada — {e}")

    # 4️⃣ Registrar servicio con costo negativo
    print("\n🔹 Caso 4: Servicio con costo negativo")
    try:
        bad_service = Service("Cambio de aceite", -50000, datetime.now().date(), "Error de costo")
        first_client = clients.first()
        first_vehicle = first_client.vehicles.first().data
        first_vehicle.add_service(bad_service)
        print("❌ ERROR: Se permitió servicio con costo negativo.")
    except Exception as e:
        print(f"✅ Correcto: Costo inválido detectado — {e}")

    # 5️⃣ Verificar ordenamiento de clientes
    print("\n🔹 Caso 5: Orden alfabético de clientes")
    clients.display_all()
    print("✅ Verifica visualmente: los clientes deben estar ordenados alfabéticamente.\n")

    # 6️⃣ Verificar orden descendente de servicios por fecha
    print("🔹 Caso 6: Orden descendente de servicios")

    if not services.is_empty():
        print("📋 Lista de servicios (orden descendente esperado):")
        last_date = None
        correctly_sorted = True

        for service in services:
            print(service)
            if last_date and service.date > last_date:
                correctly_sorted = False
            last_date = service.date

        if correctly_sorted:
            print("✅ Correcto: Servicios en orden descendente por fecha.")
        else:
            print("❌ ERROR: Servicios no están ordenados correctamente.")
    else:
        print("⚠️ No hay servicios para probar el ordenamiento.")

    print("\n================ PRUEBAS DE INSERCIÓN DE CLIENTES ================")
    client_controller = ClientController()
    try:
        cliente1 = Client("Juan Perez", "123455", "3001234567", "juan@mail.com", "Calle 1")
        client_controller.add_client(cliente1)
        print("✅ Cliente insertado correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar cliente válido: {e}")
    try:
        cliente_repetido = Client("Ana Torres", "123455", "3007654321", "ana@mail.com", "Calle 2")
        client_controller.add_client(cliente_repetido)
        print("❌ Cliente repetido insertado (debería fallar).")
    except Exception as e:
        print(f"✅ Error esperado por documento repetido: {e}")

    print("\n================ PRUEBAS DE INSERCIÓN DE VEHÍCULOS ================")
    vehicle_controller = VehicleController()
    try:
        cliente2 = Client("Isabella Diaz", "1025646344", "3206686822", "isa_diaza@gmail.com", "Carrera 56 #43-12")
        client_controller.add_client(cliente2)
        vehiculo1 = Vehicle(cliente2, "ABC-123", "Toyota", "Corolla", 2020)
        vehicle_controller.add_vehicle(vehiculo1, client_controller)
        print("✅ Vehículo insertado correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar vehículo válido: {e}")
    try:
        cliente3 = Client("Miguel Gomez", "67890", "3109876543", "migue@mail.com", "Calle 3")
        client_controller.add_client(cliente3)
        vehiculo_placa_mal = Vehicle(cliente3, "AB123", "Mazda", "3", 2021)
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

    print("\n================ PRUEBAS DE INSERCIÓN DE SERVICIOS ================")
    service_controller = ServiceController()
    try:
        servicio1 = Service("Mantenimiento", 150000, datetime(2025, 11, 5), "Cambio de aceite")
        service_controller.add_service(servicio1)
        print("✅ Servicio insertado correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar servicio válido: {e}")
    try:
        servicio_precio_neg = Service("Reparación", -50000, datetime(2025, 11, 5), "Cambio de frenos")
        service_controller.add_service(servicio_precio_neg)
        print("❌ Servicio con precio negativo insertado (debería fallar).")
    except Exception as e:
        print(f"✅ Error esperado por precio negativo: {e}")

    print("\n================ PRUEBAS DE BÚSQUEDA ================")
    cliente_encontrado = client_controller.get_client("123455")
    print("✅ Cliente encontrado:" if cliente_encontrado else "❌ Cliente no encontrado.")
    cliente_no_encontrado = client_controller.get_client("99999")
    print(
        "❌ Cliente encontrado (debería fallar)." if cliente_no_encontrado else "✅ Cliente no encontrado como se esperaba.")
    vehiculo_encontrado = vehicle_controller.get_vehicle("ABC-123")
    print("✅ Vehículo encontrado:" if vehiculo_encontrado else "❌ Vehículo no encontrado.")
    vehiculo_no_encontrado = vehicle_controller.get_vehicle("ZZZ-999")
    print(
        "❌ Vehículo encontrado (debería fallar)." if vehiculo_no_encontrado else "✅ Vehículo no encontrado como se esperaba.")
    servicio_encontrado = service_controller.get_service("Mantenimiento", "2025-11-05 00:00:00")
    print("✅ Servicio encontrado:" if servicio_encontrado else "❌ Servicio no encontrado.")
    servicio_no_encontrado = service_controller.get_service("Reparación", "2025-11-05 00:00:00")
    print(
        "❌ Servicio encontrado (debería fallar)." if servicio_no_encontrado else "✅ Servicio no encontrado como se esperaba.")

    print("\n================ PRUEBAS DE ELIMINACIÓN ================")
    try:
        client_controller.delete_client("123455")
        print("✅ Cliente eliminado correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar cliente válido: {e}")
    try:
        client_controller.delete_client("99999")
        print("❌ Cliente inexistente eliminado (debería fallar).")
    except Exception as e:
        print(f"✅ Error esperado al eliminar cliente inexistente: {e}")
    try:
        vehicle_controller.delete_vehicle("ABC-123")
        print("✅ Vehículo eliminado correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar vehículo válido: {e}")
    try:
        vehicle_controller.delete_vehicle("ZZZ-999")
        print("❌ Vehículo inexistente eliminado (debería fallar).")
    except Exception as e:
        print(f"✅ Error esperado al eliminar vehículo inexistente: {e}")
    try:
        service_controller.delete_service("Mantenimiento", "2025-11-05 00:00:00")
        print("✅ Servicio eliminado correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar servicio válido: {e}")
    try:
        service_controller.delete_service("Reparación", "2025-11-05 00:00:00")
        print("❌ Servicio inexistente eliminado (debería fallar).")
    except Exception as e:
        print(f"✅ Error esperado al eliminar servicio inexistente: {e}")

    print("\n================ PRUEBA DE INSERCIÓN ORDENADA ================")
    # Se insertan varios clientes y se imprime el orden
    nombres = ["Carlos", "Beatriz", "Andrés", "Diana"]
    for nombre in nombres:
        try:
            client_controller.add_client(Client(nombre, nombre + "_doc", "3000000000", nombre + "@mail.com", "Calle X"))
        except Exception:
            pass
    print("Clientes ordenados por nombre:")
    for cliente in clients:
        print(cliente.name)

    print("\n================ PRUEBA DE GENERACIÓN DE ARCHIVO DE CLIENTES ================")
    try:
        client_controller.to_file("another_output.txt")
        print("✅ Archivo de clientes generado correctamente.")
    except Exception as e:
        print(f"❌ Error al generar archivo de clientes: {e}")

    print("\n=== ✅ FIN DE CASOS DE PRUEBA ===\n")
