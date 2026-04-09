from modules.menu import mostrar_menu
from modules.operaciones import agregar_tarea, listar_tareas, completar_tarea
from modules.pomodoro import ejecutar_pomodoro # <--- Importación

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese la tarea: ")
            agregar_tarea(titulo)

        elif opcion == "2":
            tareas = listar_tareas()
            for t in tareas:
                estado = "✔" if t["completada"] else "✘"
                print(f"{t['id']}. {t['titulo']} [{estado}]")

        elif opcion == "3":
            id_tarea = int(input("ID de la tarea: "))
            completar_tarea(id_tarea)

        elif opcion == "4":
            # Aquí simplemente llamamos a la función
            ejecutar_pomodoro() 

        elif opcion == "5":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

  # Version 2 - Pomodoro por Deivy Vargasss