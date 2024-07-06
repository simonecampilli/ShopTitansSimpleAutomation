import pyautogui
import time

def get_mouse_position():
    try:
        while True:
            x, y = pyautogui.position()
            print(f'Position: ({x}, {y})', end="\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nInterrotto dall'utente")
time.sleep(5)
print("Posiziona il mouse sulla regione desiderata e premi Ctrl+C per interrompere.")
get_mouse_position()
