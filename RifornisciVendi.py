import pyautogui
import cv2
import numpy as np
import time

#Posizione del mouse: Point(x=451, y=124)
#Posizione del mouse: Point(x=1480, y=832)

# Funzione per trovare l'icona sullo schermo e cliccarci sopra
def find_and_click2(icon_path):
    icon_path2 = './screenshot_vendita/screenshot_9.png'
    region = (1085, 619, 331, 86)
    screen = pyautogui.screenshot(region=region)
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)

    # Carica l'icona di riferimento
    template = cv2.imread(icon_path, 0)
    w, h = template.shape[::-1]

    # Confronta l'icona con lo schermo
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where(res >= threshold)

    # Controlla se l'icona è stata trovata
    found = False
    for pt in zip(*loc[::-1]):
        found = True
        print("puoi vendere")
        break

    if not found:
        # Carica l'icona di riferimento
        '''template = cv2.imread(icon_path2, 0)
        w, h = template.shape[::-1]

        # Confronta l'icona con lo schermo
        res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = np.where(res >= threshold)

        # Controlla se l'icona è stata trovata
        found = False
        for pt in zip(*loc[::-1]):
            found = True
            print("puoi acquistare")
            break'''
        print("non puoi vendere")

    return found

time.sleep(2)
# Esempio di utilizzo
icon_path = "./screenshots_vendita/screenshot_3.png"
click_point = (100, 100)  # Questo valore non viene usato nella verifica
find_and_click2(icon_path)
