import pyautogui
import time
import os

# Coordinate dell'area da screenare
left, top, width, height = 942, 363, 230, 297
width +=50

# Funzione per fare lo screenshot dell'area specificata e salvarlo con un nome incrementale
def screenshot_region(left, top, width, height, folder_path='screenshots'):
    # Crea la cartella se non esiste
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    base_filename = 'screenshot'
    file_extension = '.png'
    file_path = os.path.join(folder_path, base_filename + file_extension)
    counter = 1

    # Incrementa il nome del file se esiste già
    while os.path.exists(file_path):
        file_path = os.path.join(folder_path, f"{base_filename}_{counter}{file_extension}")
        counter += 1

    # Cattura lo screenshot e salvalo
    region = (921, 375, 1211 - 921, 741 - 375)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(file_path)
    print(f'Screenshot salvato come {file_path}')


# Esegui lo screenshot dopo un breve ritardo per permetterti di posizionare il cursore
time.sleep(2)
screenshot_region(left, top, width, height)
