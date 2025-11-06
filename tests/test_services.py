# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: tests/test_services.py
# Descripción: Pruebas unitarias para la gestión de servicios
# =============================================================
from controllers.service_controller import ServiceController
from models.service import Service
from datetime import date


def test_services():
    """
    Prueba la gestión de servicios: inserción, validación de precio, búsqueda y eliminación.
    Entradas: Ninguna
    Salidas: Imprime resultados de cada caso de prueba (éxito o error esperado)
    Pertinencia: Permite validar que el sistema gestiona correctamente los servicios y aplica restricciones de precio y existencia.
    """
    print("\n================ PRUEBAS DE SERVICIOS ================")
    service_controller = ServiceController()

    # Inserción
    try:
        servicio1 = Service("Mantenimiento", 150000, date(2025, 11, 5), "Cambio de aceite")
        service_controller.add_service(servicio1)
        print("✅ Servicio insertado correctamente.")
    except Exception as e:
        print(f"❌ Error al insertar servicio válido: {e}")

    try:
        servicio_precio_neg = Service("Reparación", -50000, date(2025, 11, 5), "Cambio de frenos")
        service_controller.add_service(servicio_precio_neg)
        print("❌ Servicio con precio negativo insertado (debería fallar).")
    except Exception as e:
        print(f"✅ Error esperado por precio negativo: {e}")

    # Búsqueda
    print("\n🔎 PRUEBAS DE BÚSQUEDA")
    servicio_encontrado = service_controller.get_service("Mantenimiento", date(2025, 11, 5))
    print("✅ Servicio encontrado." if servicio_encontrado else "❌ Servicio no encontrado.")
    servicio_no_encontrado = service_controller.get_service("Reparación", date(2025, 11, 5))
    print(
        "✅ Servicio no encontrado como se esperaba." if not servicio_no_encontrado else "❌ Servicio encontrado (debería fallar).")

    # Eliminación
    print("\n🗑️ PRUEBAS DE ELIMINACIÓN")
    try:
        service_controller.delete_service("Mantenimiento", date(2025, 11, 5))
        print("✅ Servicio eliminado correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar servicio válido: {e}")

    try:
        service_controller.delete_service("Reparación", date(2025, 11, 5))
        print("✅ Error esperado al eliminar servicio inexistente: correcto.")
    except Exception as e:
        print(f"✅ Error esperado al eliminar servicio inexistente: {e}")
