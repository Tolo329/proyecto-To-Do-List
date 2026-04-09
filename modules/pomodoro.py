import time 
from plyer import notification 

def ejecutar_pomodoro():
    print("\n>>> Temporizador iniciado: 25 min de trabajo.")
    time.sleep(1500) # 25 minutos
    notification.notify(
        title = "Pomodoro 25",
        message = "¡Es tiempo de descansar!",
        timeout = 10
    )
    
    print(">>> Iniciando 5 min de descanso.")
    time.sleep(300) # 5 minutos
    notification.notify(
        title = "Pomodoro 5",
        message = "¡Es hora de trabajar otra vez!",
        timeout = 10
    )
    print(">>> Ciclo completado. Volviendo al menú...")