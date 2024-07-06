import pyautogui
import time


OGGETTI = 3
TEMPO = 3*60+38
N_VOLTE = 4
def oggetto_raro():
    pyautogui.moveTo(800,773)#Point(x=800, y=773) oggetto raro sbloccato
    pyautogui.click() #ok oggetto raro
    pyautogui.moveTo(802, 783)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(954, 968)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(1027,984)
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(1207, 784)
    time.sleep(0.5)
    pyautogui.click()




def presa():
    pyautogui.moveTo(1680, 966)
    time.sleep(1)
    pyautogui.click()
# Sposta il mouse alle coordinate x=100, y=100 (puoi cambiare i valori)
time.sleep(5)
for y in range(N_VOLTE):

    print("apertura Menu")
    pyautogui.moveTo(1798, 962)
    time.sleep(1)
    # Clic sinistro del mouse
    pyautogui.click()  # Clicca con il tasto sinistro del mouse
    time.sleep(1)
    print("Pick oggetto")
    #pyautogui.moveTo(304,776)  #x=506, y=806  304, 776
    #pyautogui.moveTo(506, 806)

    pyautogui.moveTo(712, 791)

    for y in range(OGGETTI):
        time.sleep(1)
        pyautogui.click()
    print("oggetti selezionati, inizio produzione")
    time.sleep(TEMPO)
    print("OGGETTO PRODOTTO, PRESA")
    for y in range(OGGETTI):
        presa()
        #time.sleep(1)
        oggetto_raro()
        #time.sleep(1)

    #----------------


    #RESET
    pyautogui.moveTo(229, 93)
    pyautogui.click()


