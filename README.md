# BR-AutoGrind
Please note this is made by AI.

## Overview

This project automates the control of a train simulation application using Python. It utilizes Optical Character Recognition (OCR) to read critical data from the screen, such as distance to the next station, current speed, and speed limit. The program also interacts with the user interface through mouse clicks and keyboard inputs.

## Features

- Clicks on specific pixel positions in the UI to navigate through menus.
- Takes screenshots of defined screen portions to extract text data using OCR.
- Calculates route ratios and determines optimal paths based on the extracted data.
- Controls train acceleration and deceleration based on distance, speed, and speed limits.
- Opens train doors when the train is fully in a station and waits for loading completion.

## Requirements

- Python 3.x
- `pytesseract` for OCR functionality
- `opencv-python` for image processing
- `pyautogui` for taking screenshots and simulating mouse clicks
- `keyboard` for simulating keyboard inputs
- Tesseract-OCR installed on your system

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/train-control-automation.git
   cd train-control-automation
