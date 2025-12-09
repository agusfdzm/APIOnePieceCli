import requests

BASE = "https://api.api-onepiece.com/v2"

def listar_personajes(limit=10):
    url = f"{BASE}/characters/en"
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
    except requests.exceptions.Timeout:
        print("La petición ha tardado mucho.")
        return []
    except requests.exceptions.HTTPError as e:
        print("Error HTTP: {r.status_code}")
        return []
    
    data = r.json()
    return data[:limit]

personajes = listar_personajes(limit=5)

if personajes:
    print("Personajes: ")
    for personaje in personajes:
        nombre = personaje.get('name', 'Nombre desconocido')
        print(f"-> {nombre}")