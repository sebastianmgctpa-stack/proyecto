import json
import os

# Nombre del archivo de datos
ARCHIVO_DATOS = "eventos.json"

# Cargar los eventos desde el archivo JSON
def cargar_eventos():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []  # Si no existe, retorna una lista vacía

# Guardar la lista de eventos en el archivo JSON
def guardar_eventos(eventos):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(eventos, f, indent=4, ensure_ascii=False)

# Generar el siguiente código de evento (EVT001, EVT002, ...)
def generar_codigo(eventos):
    if not eventos:
        return "EVT001"
    ultimo = max(int(e["codigo"][3:]) for e in eventos)
    return f"EVT{ultimo + 1:03d}"