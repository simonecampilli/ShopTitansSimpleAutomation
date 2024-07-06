import pyautogui
import cv2
import numpy as np
import time
from RifornisciVendi import find_and_click2
from acquista import find_and_click3

ICON_PATH = "./screenshots_vendita/screenshot_3.png"
ICON_PATH2 = " /screenshots_vendita/screenshot_9.png"
left, top, width, height = 942, 363, 230, 297
width +=50
# Funzione per trovare l'icona sullo schermo e cliccarci sopra
def find_and_click(icon_path, click_point):
    region = (921, 375, 1211 - 921, 741 - 375)
    screen = pyautogui.screenshot(region=region)
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)

    # Carica l'icona di riferimento
    template = cv2.imread(icon_path, 0)
    w, h = template.shape[::-1]

    # Confronta l'icona con lo schermo
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.4
    loc = np.where(res >= threshold)

    # Controlla se l'icona è stata trovata
    found = False
    for pt in zip(*loc[::-1]):
        found = True
        print("Icona trovata a:", pt)
        time.sleep(2)
        pyautogui.moveTo(977, 529)
        pyautogui.click()
        for y in range(7):
            time.sleep(2)
            if find_and_click2(ICON_PATH):
                pyautogui.moveTo(1271, 662)
                pyautogui.click()
            #if find_and_click3(ICON_PATH):
                ##pyautogui.moveTo(1271, 662)
                #pyautogui.click()
            else:
                pyautogui.moveTo(693, 668)
                pyautogui.click()



        break

    if not found:
        print("Icona non trovata.")

    return found
while True:


    # Esempio di utilizzo
    icon_path = "./screenshots/screenshot_1.png"
    click_point = (100, 100)  # Questo valore non viene usato nella verifica
    find_and_click(icon_path, click_point)
    time.sleep(2 * 60)