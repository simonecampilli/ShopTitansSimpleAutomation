# Automated Screen Interaction Project

## Introduction

This project focuses on automating interactions with screen elements using various Python scripts. The primary tasks include taking screenshots, recognizing and clicking specific icons, and performing repetitive actions based on recognized screen elements.

## Files and Their Functions

### `main.py`
This script obtains the current mouse position and prints it. It is useful for identifying coordinates for screen interactions.

### `posizione.py`
A script to continuously print the current mouse position, allowing the user to identify specific areas on the screen by moving the mouse.

### `screenshot.py`
Takes a screenshot of a specified region on the screen and saves it with an incremented filename. It helps in capturing and saving visual data from the screen.

### `acquista.py`
Contains a function to find and click on a specified icon within a region on the screen. It uses OpenCV for image recognition and PyAutoGUI for interacting with the screen.

### `RifornisciVendi.py`
Similar to `acquista.py`, this script finds an icon on the screen and clicks it, indicating the ability to handle both buying and selling actions.

### `script.py`
Automates a sequence of interactions, such as moving the mouse to specific coordinates and clicking. It is designed for repetitive tasks involving multiple objects and time delays.

### `Riconoscimento.py`
Combines the functionalities of `acquista.py` and `RifornisciVendi.py` to recognize icons and perform click actions. It runs in a loop, checking for the presence of specific icons and acting accordingly.

### `NumberRecognition.py`
Uses Tesseract OCR to recognize numbers in a given image. It processes the image, extracts text, and filters out numeric values.

## Libraries Used

- **pyautogui**: For automating mouse and keyboard actions.
- **cv2 (OpenCV)**: For image processing and template matching.
- **numpy**: For numerical operations.
- **time**: For introducing delays.
- **os**: For file operations.
- **PIL (Python Imaging Library)**: For handling image files.
- **pytesseract**: For Optical Character Recognition (OCR).

## How to Use

1. **Setup**:
   - Install required libraries using `pip install pyautogui opencv-python numpy pillow pytesseract`.

2. **Run the Scripts**:
   - Identify the screen regions and coordinates using `main.py` and `posizione.py`.
   - Use `screenshot.py` to capture screenshots of the desired regions.
   - Modify the `icon_path` and coordinates in `acquista.py`, `RifornisciVendi.py`, and `Riconoscimento.py` to match your screen setup.
   - Execute `script.py` to automate the series of actions for object handling.

3. **OCR**:
   - Ensure Tesseract is installed and the path is correctly set in `NumberRecognition.py`.
   - Place the image to be recognized in the specified path and run the script to extract numbers.

## Example Workflow

1. Use `posizione.py` to find the coordinates of elements on the screen.
2. Capture these regions with `screenshot.py`.
3. Update the `icon_path` in `acquista.py` and `RifornisciVendi.py` with the captured screenshots.
4. Execute `Riconoscimento.py` to continuously monitor and interact with the screen elements.
5. Use `script.py` to automate repetitive tasks involving the recognized elements.
6. Employ `NumberRecognition.py` for tasks requiring text extraction from images.

## Acknowledgements

- The project leverages various Python libraries to achieve screen automation and image recognition.
- OpenCV and Tesseract OCR are instrumental in the image processing and recognition tasks.

-----------------------------------------------------------------------------------------


# Progetto di Interazione Automatica con lo Schermo

## Introduzione

Questo progetto si concentra sull'automazione delle interazioni con gli elementi dello schermo utilizzando vari script Python. I compiti principali includono catturare screenshot, riconoscere e cliccare su icone specifiche, ed eseguire azioni ripetitive basate su elementi riconosciuti sullo schermo.

## File e le Loro Funzioni

### `main.py`
Questo script ottiene la posizione attuale del mouse e la stampa. È utile per identificare le coordinate per le interazioni sullo schermo.

### `posizione.py`
Uno script che stampa continuamente la posizione attuale del mouse, permettendo all'utente di identificare aree specifiche sullo schermo muovendo il mouse.

### `screenshot.py`
Cattura uno screenshot di una regione specificata sullo schermo e lo salva con un nome incrementale. Aiuta a catturare e salvare dati visivi dallo schermo.

### `acquista.py`
Contiene una funzione per trovare e cliccare su un'icona specificata all'interno di una regione sullo schermo. Utilizza OpenCV per il riconoscimento delle immagini e PyAutoGUI per interagire con lo schermo.

### `RifornisciVendi.py`
Simile a `acquista.py`, questo script trova un'icona sullo schermo e la clicca, indicando la capacità di gestire sia azioni di acquisto che di vendita.

### `script.py`
Automatizza una sequenza di interazioni, come spostare il mouse a coordinate specifiche e cliccare. È progettato per compiti ripetitivi che coinvolgono più oggetti e ritardi temporali.

### `Riconoscimento.py`
Combina le funzionalità di `acquista.py` e `RifornisciVendi.py` per riconoscere le icone ed eseguire azioni di clic. Funziona in un ciclo, controllando la presenza di icone specifiche e agendo di conseguenza.

### `NumberRecognition.py`
Utilizza Tesseract OCR per riconoscere i numeri in un'immagine data. Elabora l'immagine, estrae il testo e filtra i valori numerici.

## Librerie Utilizzate

- **pyautogui**: Per automatizzare le azioni del mouse e della tastiera.
- **cv2 (OpenCV)**: Per l'elaborazione delle immagini e il template matching.
- **numpy**: Per le operazioni numeriche.
- **time**: Per introdurre ritardi.
- **os**: Per le operazioni sui file.
- **PIL (Python Imaging Library)**: Per gestire i file di immagini.
- **pytesseract**: Per il riconoscimento ottico dei caratteri (OCR).

## Come Usare

1. **Configurazione**:
   - Installa le librerie necessarie usando `pip install pyautogui opencv-python numpy pillow pytesseract`.

2. **Esegui gli Script**:
   - Identifica le regioni dello schermo e le coordinate utilizzando `main.py` e `posizione.py`.
   - Usa `screenshot.py` per catturare screenshot delle regioni desiderate.
   - Modifica il `icon_path` e le coordinate in `acquista.py`, `RifornisciVendi.py` e `Riconoscimento.py` per adattarli alla tua configurazione dello schermo.
   - Esegui `script.py` per automatizzare la serie di azioni per la gestione degli oggetti.

3. **OCR**:
   - Assicurati che Tesseract sia installato e che il percorso sia correttamente impostato in `NumberRecognition.py`.
   - Posiziona l'immagine da riconoscere nel percorso specificato ed esegui lo script per estrarre i numeri.

## Esempio di Workflow

1. Usa `posizione.py` per trovare le coordinate degli elementi sullo schermo.
2. Cattura queste regioni con `screenshot.py`.
3. Aggiorna il `icon_path` in `acquista.py` e `RifornisciVendi.py` con gli screenshot catturati.
4. Esegui `Riconoscimento.py` per monitorare e interagire continuamente con gli elementi dello schermo.
5. Usa `script.py` per automatizzare i compiti ripetitivi che coinvolgono gli elementi riconosciuti.
6. Utilizza `NumberRecognition.py` per compiti che richiedono l'estrazione di testo dalle immagini.

## Ringraziamenti

- Il progetto sfrutta varie librerie Python per ottenere l'automazione dello schermo e il riconoscimento delle immagini.
- OpenCV e Tesseract OCR sono strumentali nei compiti di elaborazione e riconoscimento delle immagini.

