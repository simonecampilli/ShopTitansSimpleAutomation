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
