"""
Nom du Script : auto_screenshot.py
Auteur :        Thomas Bocande
Description :   Produit des captures d'écran à un certain rythme
"""

import time
import os
import threading
from pynput.keyboard import Listener, KeyCode
from PIL import ImageGrab


## Variables globales
capture = False
end = False


## Fonctions spécifiques à l'OS
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def getDelimit():
    if os.name == 'nt':
        delimit = "\\"
    else:
        delimit = "/"
    return str(delimit)

DELIMIT = getDelimit()

clear()


## Variables de configuration et initialisation
GAME_NAME = input("Nom du jeu : ")
MAX_ITER = int(input("Nombre de captures : "))
FREQUENCY = int(input("Fréquence de capture (images/min) : "))
TIME = int(60 / FREQUENCY)

toggle = input("Touche de capture : ")
stop = input("Touche d'arrêt : ")

TOGGLE_KEY = KeyCode(char=toggle)
EXIT_KEY = KeyCode(char=stop)

START_INDEX = int(input("Index de départ : "))

clear()
print("Initialisation....")

PATH = os.getcwd() + DELIMIT + GAME_NAME
    
os.makedirs(PATH, exist_ok=True)


def screenshot(stop_event):
    i = START_INDEX
    maxIter = MAX_ITER + START_INDEX
    while i < maxIter:
        if end:
            break
        if capture:
            clear()
            # Capture the entire screen
            screenshot = ImageGrab.grab()
            # Save the screenshot to a file
            screenshot.save(PATH + DELIMIT + GAME_NAME + "_" + str(i) + ".png")
            # Close the screenshot
            screenshot.close()

            print("---- *click* ----")
            print("Capture " + str(i) + "/" + str(maxIter))
            print("Temps restant : " + str((maxIter - i) * TIME) + " secondes")
            print("-----------------")
            i += 1
            time.sleep(TIME)
    stop_event.set()
    print("Fin de la capture !")
    return


## Gestions du thread et du listener
def toggle_event(key, stop_event):
    if key == TOGGLE_KEY:
        global capture
        capture = not capture
        print("Pause")
    if key == EXIT_KEY:
        global end
        end = not end
        stop_event.set()
        print("Arrêt...")

stop_event = threading.Event()
capture_thread = threading.Thread(target=screenshot, args=(stop_event,))
capture_thread.start()

print("Prêt !")

with Listener(on_press=lambda key: toggle_event(key, stop_event)) as listener:
    while not stop_event.is_set():
        time.sleep(1)