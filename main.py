from modules.menu import mostrar_menu
from modules.operaciones import agregar_tarea, listar_tareas, completar_tarea
<<<<<<< HEAD
from modules.pomodoro import ejecutar_pomodoro # <--- Importación
=======
from modules.pomodoro import ejecutar_pomodoro
from modules.prioridad import establecer_tarea_del_dia # <-- Nueva importación
>>>>>>> 2cdbb73 (Entrega Integrante 3: Integración de Prioridad de Tarea)

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
<<<<<<< HEAD
            id_tarea = int(input("ID de la tarea: "))
            completar_tarea(id_tarea)

        elif opcion == "4":
            # Aquí simplemente llamamos a la función
            ejecutar_pomodoro() 

        elif opcion == "5":
=======
            try:
                id_tarea = int(input("ID de la tarea: "))
                completar_tarea(id_tarea)
            except ValueError:
                print("ID no válido.")

        elif opcion == "4":
            ejecutar_pomodoro()

        elif opcion == "5":
            # Llamamos a la nueva función
            establecer_tarea_del_dia()

        elif opcion == "6":
            print("¡Hasta luego!")
>>>>>>> 2cdbb73 (Entrega Integrante 3: Integración de Prioridad de Tarea)
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
<<<<<<< HEAD
    main()

  # Version 2 - Pomodoro por Deivy Vargasss
=======
    main()
>>>>>>> 2cdbb73 (Entrega Integrante 3: Integración de Prioridad de Tarea)
