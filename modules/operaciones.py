from utils.archivos import leer_datos, guardar_datos

def agregar_tarea(titulo):
    datos = leer_datos()
    tarea = {
        "id": len(datos) + 1,
        "titulo": titulo,
        "completada": False
    }
    datos.append(tarea)
    guardar_datos(datos)

def listar_tareas():
    return leer_datos()

def completar_tarea(id_tarea):
    datos = leer_datos()
    for tarea in datos:
        if tarea["id"] == id_tarea:
            tarea["completada"] = True
    guardar_datos(datos)