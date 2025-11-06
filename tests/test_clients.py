# =============================================================
# Momento Evaluativo 4 - Estructura de Datos y Laboratorio
#
# Integrantes:
#   - Santiago Molano Holguín
#   - Samuel Olaya Olaya
#   - Kevin Álvarez Blandon
#
# Docente: Ricardo Franco Ceballos - ITM
# Archivo: tests/test_clients.py
# Descripción: Pruebas unitarias para la gestión de clientes
# =============================================================
from controllers.client_controller import ClientController
from models.client import Client


def test_clients():
    """
    Prueba la gestión de clientes: inserción, búsqueda, eliminación y validación de duplicados.
    Entradas: Ninguna
    Salidas: Imprime resultados de cada caso de prueba (éxito o error esperado)
    Pertinencia: Permite validar que el sistema gestiona correctamente los clientes y aplica restricciones como unicidad y existencia.
    """
    print("\n================ PRUEBAS DE CLIENTES ================")
    client_controller = ClientController()

    # Inserción
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

    # Búsqueda
    print("\n🔎 PRUEBAS DE BÚSQUEDA")
    cliente_encontrado = client_controller.get_client("123455")
    print("✅ Cliente encontrado." if cliente_encontrado else "❌ Cliente no encontrado.")
    cliente_no_encontrado = client_controller.get_client("99999")
    print(
        "✅ Cliente no encontrado como se esperaba." if not cliente_no_encontrado else "❌ Cliente encontrado (debería fallar).")

    # Eliminación
    print("\n🗑️ PRUEBAS DE ELIMINACIÓN")
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

    # Inserción ordenada
    print("\n📋 PRUEBA DE INSERCIÓN ORDENADA")
    try:
        client_controller.add_client(Client("Zacarías", "zac_doc", "3001111111", "zac@mail.com", "Calle 3"))
        client_controller.add_client(Client("Alejandro", "ale_doc", "3002222222", "ale@mail.com", "Calle 4"))
        client_controller.add_client(Client("Beatriz", "bea_doc", "3003333333", "bea@mail.com", "Calle 5"))
    except Exception as e:
        raise AssertionError(f"Error al insertar clientes ordenados: {e}") from e
    print("Clientes ordenados por nombre:")
    for cliente in client_controller:
        print(cliente.name)
