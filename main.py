import cv2
import time
import pygetwindow as gw
from funciones import emulador
from buscar import analizar

def main():
    emulador()
    contador = 0
    shiny = False
    image_path = cv2.imread('C:/Users/arnov/Documents/Python/Shiny/Imagenes/Estatico.PNG')#ruta del sprite png

    # Abrir en primer plano la aplicación
    time.sleep(2)
    ventana = gw.getWindowsWithTitle('VisualBoyAdvance')[0]
    ventana.activate() 

    # Realiza la búsqueda en la ventana de la imagen
    tiempo_inicio = time.time()
    while True:
        contador += 1
        shiny = analizar(image_path, contador, shiny, tiempo_inicio, ventana)
        if shiny:
            print("***ES SHINYYYYYY!!!!!!!!***")
            break  # Sal del bucle si encuentras un shiny

if __name__ == '__main__':
    main()