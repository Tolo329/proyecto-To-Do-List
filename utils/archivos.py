import json

RUTA = "data/datos.json"

def leer_datos():
    try:
        with open(RUTA, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_datos(datos):
    with open(RUTA, "w") as f:
        json.dump(datos, f, indent=4)