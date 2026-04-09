import json
from utils.archivos import guardar_datos # Reutilizamos tu lógica de guardado

RUTA_PRIORIDAD = "data/prioridad.json"

def establecer_tarea_del_dia():
    """Lógica para elegir la tarea más importante del día."""
    lista = []
    print("\n👋 ¡Hola! Vamos a organizar tu día.")
    print("Introduce tus actividades (escribe 'fin' para terminar):")
    
    while True:
        tarea = input("- ")
        if tarea.lower() == 'fin':
            break
        if tarea.strip(): 
            lista.append(tarea)
    
    if not lista:
        print("No agregaste ninguna actividad.")
        return

    print("\n--- Estas son tus actividades ---")
    for i, tarea in enumerate(lista):
        print(f"{i + 1}. {tarea}")

    try:
        opcion = int(input("\n¿Cuál es la más importante? (Escribe el número): "))
        if 1 <= opcion <= len(lista):
            seleccionada = lista[opcion - 1]
            
            # Guardamos en un archivo separado para no mezclar con la to-do list general
            datos = {"actividad_del_dia": seleccionada}
            with open(RUTA_PRIORIDAD, "w") as f:
                json.dump(datos, f, indent=4)
                
            print(f"\n✨ ¡Excelente! '{seleccionada}' es ahora tu ACTIVIDAD DEL DÍA.")
        else:
            print("Ese número no está en la lista.")
    except ValueError:
        print("Por favor, introduce un número válido.")