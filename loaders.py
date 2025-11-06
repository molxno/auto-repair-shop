# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: loaders.py
# Descripción: Cargador de datos desde archivos CSV.
# =============================================================
from controllers.client_controller import ClientController
from controllers.vehicle_controller import VehicleController
from controllers.service_controller import ServiceController
from models.client import Client
from models.vehicle import Vehicle
from models.service import Service
from datetime import datetime


def cargar_clientes(controller: ClientController, file_name: str):
    """
    Carga los clientes desde un archivo CSV y los agrega a la lista doble gestionada por el controlador.
    Entradas: controller (ClientController), file_name (str, ruta del archivo CSV)
    Salidas: Ninguna (los clientes se agregan al controlador, imprime mensajes de éxito o error)
    Pertinencia: Permite la carga masiva y automatizada de clientes, facilitando la gestión y validación de datos en el sistema.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            next(file)  # saltar encabezado
            for linea in file:
                datos = linea.strip().split(";")
                if len(datos) < 5:
                    continue

                name, document, phone, email, address = datos[:5]
                client = Client(name, document, phone, email, address)
                controller.add_client(client)

        print(f"✅ Clientes cargados desde {file_name}")
    except Exception as error:
        print(f"❌ Error al leer {file_name}: {error}")


def cargar_vehiculos(controller: VehicleController, client_controller: ClientController, file_name: str):
    """
    Carga los vehículos desde un archivo CSV, los asocia a clientes existentes y los agrega a la lista doble gestionada por el controlador.
    Entradas: controller (VehicleController), client_controller (ClientController), file_name (str, ruta del archivo CSV)
    Salidas: Ninguna (los vehículos se agregan al controlador y al cliente, imprime mensajes de éxito o error)
    Pertinencia: Permite la carga masiva y automatizada de vehículos, asegurando la relación con clientes y la validación de datos.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            next(file)
            for linea in file:
                datos = linea.strip().split(";")
                if len(datos) < 5:
                    continue

                document, plate, brand, model, year = datos
                year = int(year)

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
    """
    Carga los servicios desde un archivo CSV, los asocia a los vehículos y los agrega a la lista doble gestionada por el controlador.
    Entradas: controller (ServiceController), vehicle_controller (VehicleController), file_name (str, ruta del archivo CSV)
    Salidas: Ninguna (los servicios se agregan al controlador y al vehículo, imprime mensajes de éxito o error)
    Pertinencia: Permite la carga masiva y automatizada de servicios, facilitando la gestión y validación de mantenimientos en el sistema.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            next(file)
            for linea in file:
                datos = linea.strip().split(";")
                if len(datos) < 5:
                    continue

                plate, type_service, price, date_str, description = datos
                price = float(price)
                date = datetime.strptime(date_str, "%d/%m/%Y").date()

                service = Service(type_service, price, date, description)
                controller.add_service(service)
                vehicle_controller.add_service_to_vehicle(plate, service)

        print(f"✅ Servicios cargados desde {file_name}")
    except Exception as error:
        print(f"❌ Error al leer {file_name}: {error}")
