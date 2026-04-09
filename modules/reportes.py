from utils.archivos import leer_datos

def tareas_completadas():
    datos = leer_datos()
    return sum(1 for t in datos if t["completada"])