Proyecto: Lista de Tareas + Pomodoro 📝

Este es un programa básico de consola hecho en Python para gestionar tareas pendientes y mejorar la concentración usando la técnica Pomodoro.
 
¿Qué puedes hacer?

    Gestionar tareas: Agregar, ver y marcar tareas como terminadas.

    Temporizador Pomodoro: Un cronómetro de 25 minutos para trabajar y 5 para descansar.

    Tarea del Día: Una función especial para elegir y guardar tu actividad más importante.

Organización de los archivos

El código está dividido para que sea más fácil de leer:

    main.py: Es el archivo principal que debes ejecutar.

    modules/: Aquí están las funciones del menú, el pomodoro y las tareas.

    utils/: Contiene el código para guardar la información.

    data/: Aquí se crean los archivos .json donde se guardan tus tareas.

Cómo hacerlo funcionar

Para que el programa pueda enviar notificaciones a tu computadora, necesitas instalar una librería llamada plyer.

    Instalar la librería:
    Abre una terminal y escribe:

    pip install plyer
    

    Correr el programa:
    Escribe en la terminal:

    python main.py

 Notas

    Los datos se guardan automáticamente en la carpeta data. No borres esa carpeta para no perder tus tareas.

    Si usas Windows, las notificaciones del Pomodoro aparecerán en la esquina de tu pantalla.
    
Integrantes:

Alan Romero - Estructura básica de To-Do List
Deivy Vargas - Integración de Temporizador Pomodoro
Luis Luquez - Integración de Prioridad de Tarea
