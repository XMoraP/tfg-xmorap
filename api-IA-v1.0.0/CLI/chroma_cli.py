import chromadb
import sys

CHROMA_PATH = "../../database"  

def list_collections():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collections = client.list_collections()

    if not collections:
        print("❌ No se encontraron colecciones en la base de datos.")
        return

    print("📦 Colecciones disponibles en ChromaDB:\n")
    for name in collections:
      print(f"→ {name}")

def delete_collection(name):
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    try:
        client.delete_collection(name=name)
        print(f"✅ Colección '{name}' eliminada correctamente.")
    except Exception as e:
        print(f"❌ Error al eliminar la colección '{name}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ Uso: python chroma_cli.py [list|delete <nombre_coleccion>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_collections()

    elif command == "delete":
        if len(sys.argv) < 3:
            print("❗ Uso: python chroma_cli.py delete <nombre_coleccion>")
            sys.exit(1)
        collection_name = sys.argv[2]
        delete_collection(collection_name)

    else:
        print(f"❌ Comando no reconocido: {command}")
        print("🧰 Comandos disponibles: list, delete <nombre_coleccion>")
