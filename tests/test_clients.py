# =============================================================
# Archivo: tests/test_clients.py
# Descripción: Pruebas unitarias para la gestión de clientes
# =============================================================
from controllers.client_controller import ClientController
from models.client import Client


def test_clients():
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
    except Exception:
        pass
    print("Clientes ordenados por nombre:")
    for cliente in client_controller:
        print(cliente.name)

    # Generación de archivo
    print("\n💾 PRUEBA DE GENERACIÓN DE ARCHIVO")
    try:
        client_controller.to_file("another_output.txt")
        print("✅ Archivo de clientes generado correctamente.")
    except Exception as e:
        print(f"❌ Error al generar archivo de clientes: {e}")
