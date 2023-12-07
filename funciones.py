import subprocess
import time
import pyautogui

EMULATOR_PATH = "C:/Users/arnov/Documents/pokemon/VisualBoyAdvance.exe"
ROM_PATH = "C:/Users/arnov/Documents/pokemon/juegos/Esmeralda_Crianza.zip"
RESET_HOTKEY = 'ctrl+r'

def emulador():
    """Abre el emulador con el juego."""
    subprocess.Popen([EMULATOR_PATH, ROM_PATH], shell=True)
    time.sleep(2)

def reset():
    """Realiza el soft-reset."""
    pyautogui.hotkey(*RESET_HOTKEY.split('+'))

def pulsar_z(times=2):
    """Presiona 'z' varias veces."""
    for _ in range(times):
        pyautogui.keyDown("z")
        pyautogui.keyUp("z")
        time.sleep(0.5)

def carga_inicial(times=4):
    """Realiza la carga inicial."""
    time.sleep(0.5)
    for _ in range(times):
        pyautogui.keyDown('z')
        pyautogui.keyUp('z')
        time.sleep(0.5)