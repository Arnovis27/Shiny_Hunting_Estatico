import time
import pyautogui
import funciones

def analizar(image_path, contador, shiny, tiempo_inicio, ventana):
    funciones.carga_inicial()
    time.sleep(0.5)
    funciones.pulsar_z()

    if ventana:
        # Obtener las coordenadas de la ventana
        left, top, width, height = ventana.left, ventana.top, ventana.width, ventana.height
        # Calcular las coordenadas relativas al centro de la ventana
        center_x, center_y = left + width // 2, top + height // 2

        # Hacer clic en el centro de la ventana
        pyautogui.click(center_x, center_y)

        # Buscar la imagen en la pantalla centrada en la ventana
        time.sleep(1)
        location = pyautogui.locateOnScreen(image_path)

        # Ver las coordenadas de la ubicación
        shiny = True if location is None else False

        # Obtener el tiempo de ejecución
        tiempo_fin = time.time()
        total_segundos = tiempo_fin - tiempo_inicio
        horas, rem = divmod(total_segundos, 3600)
        minutos, segundos = divmod(rem, 60)

        print(f"Encuentros: {contador}, Tiempo de ejecución: {int(horas)} horas, {int(minutos)} minutos, {int(segundos)} segundos")

        if not shiny:
            funciones.reset()#soft-reset

    return shiny