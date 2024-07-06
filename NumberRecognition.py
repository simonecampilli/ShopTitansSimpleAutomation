from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import cv2
import numpy as np
import pytesseract

# Imposta il percorso al binario di tesseract, se necessario
# pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract_executable'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Carica l'immagineimage_path = './Numeri/img.png'


import pytesseract
from PIL import Image
import cv2
import numpy as np

# Imposta il percorso al binario di tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Carica l'immagine

image_path = './Numeri/img.png'
image = Image.open(image_path)
image = cv2.imread(image_path)

# Controlla se l'immagine è stata caricata correttamente
if image is None:
    raise FileNotFoundError(f"Impossibile trovare o caricare l'immagine dal percorso: {image_path}")

# Converti l'immagine in scala di grigi
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applica una soglia per ottenere un'immagine binaria
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Trova i contorni delle regioni di interesse (i numeri)
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

numbers = []

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if h > 10:  # filtro per evitare contorni troppo piccoli
        roi = image[y:y+h, x:x+w]
        roi_pil = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))

        # Utilizza pytesseract per riconoscere il testo
        custom_oem_psm_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(roi_pil, config=custom_oem_psm_config)

        # Filtra solo i numeri dal testo riconosciuto
        detected_numbers = [int(s) for s in text.split() if s.isdigit()]
        numbers.extend(detected_numbers)

print("Numeri riconosciuti:", numbers)