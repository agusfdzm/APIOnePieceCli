import requests
import sys

BASE = "https://api.api-onepiece.com/v2"


def listar_personajes(limit=10):
    try:
        r = requests.get(f"{BASE}/characters/en", timeout=10)
        r.raise_for_status()
        return r.json()[:limit]
    except Exception as e:
        print("Error al listar personajes:", e)
        return []


def buscar_personaje(nombre):
    try:
        r = requests.get(f"{BASE}/characters/en/search", params={"name": nombre}, timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Error al buscar personaje:", e)
        return []


def obtener_personaje_por_id(pid):
    try:
        r = requests.get(f"{BASE}/characters/en/{pid}", timeout=10)
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print("Error al obtener personaje por ID:", e)
        return None


def mostrar_lista(lista):
    if not lista:
        print("No hay resultados.")
        return
    for i, p in enumerate(lista, start=1):
        print(f"{i}. {p.get('name', '<sin nombre>')} (ID: {p.get('id')})")


def mostrar_detalle(p):
    if not p:
        print("Personaje no encontrado.")
        return
    print(f"Nombre: {p.get('name')}")
    print(f"ID: {p.get('id')}")
    if p.get('description'):
        print(f"Descripción: {p.get('description')}")


def main():
    while True:
        print("\nOnePieceAPI - opciones:")
        print("1) Listar personajes")
        print("2) Buscar por nombre")
        print("3) Obtener por ID")
        print("4) Salir")
        opcion = input("Elige una opción: ").strip()
        if opcion == '1':
            lim = input("Límite (enter=10): ").strip()
            try:
                lim = int(lim) if lim else 10
            except ValueError:
                lim = 10
            lista = listar_personajes(limit=lim)
            mostrar_lista(lista)
        elif opcion == '2':
            q = input("Nombre: ").strip()
            if not q:
                print("Nombre vacío")
                continue
            resultados = buscar_personaje(q)
            mostrar_lista(resultados)
        elif opcion == '3':
            pid = input("ID: ").strip()
            if not pid:
                print("ID vacío")
                continue
            p = obtener_personaje_por_id(pid)
            mostrar_detalle(p)
        elif opcion == '4':
            print("Adiós")
            return
        else:
            print("Opción inválida")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaliendo...")
        sys.exit(0)
