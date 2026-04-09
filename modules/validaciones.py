def validar_opcion(opcion):
    return opcion.isdigit() and 1 <= int(opcion) <= 4

def validar_texto(texto):
    return len(texto.strip()) > 0