# BR AutoGrind

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

## Installation Instructions

### Step 1: Clone the Repository

Open your terminal and run the following command to clone the repository:

```bash
git clone https://github.com/yourusername/train-control-automation.git
cd train-control-automation
```

### Step 2: Install Python Packages

Ensure you have `pip` installed, then run:

```bash
pip install pytesseract opencv-python pyautogui keyboard
```

### Step 3: Install Tesseract-OCR

#### For Windows:
1. Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
2. Install it and note the installation path (e.g., `C:\Program Files\Tesseract-OCR`).
3. Add the Tesseract installation path to your system's PATH environment variable.

#### For macOS:
Use Homebrew to install Tesseract:

```bash
brew install tesseract
```

#### For Linux:
Install Tesseract using the package manager:

```bash
sudo apt-get install tesseract-ocr
```

### Step 4: Configure Tesseract Path in Code

If Tesseract is not in your system's PATH, set its path in your script:

In `drive.py`, add the following line:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your path
```

### Step 5: Configure Pixel Positions

Open `config.py` and set the pixel positions and parameters according to your application’s UI layout. Make sure to adjust values like `drivePos`, `loadConsistPos`, and other portions to match the actual coordinates on your screen.

## Usage Instructions

1. **Start the Application**: Run the main script:

   ```bash
   python main.py
   ```

2. **Control the Automation**:
   - Press **`s`** to start the train control process.
   - Press **`e`** to stop the automation at any time.

3. **Monitor Output**: The program will log its actions in the console. Check for any errors or required adjustments based on your screen's response.

## Code Structure

- **`config.py`**: Contains configuration variables such as pixel positions and control parameters.
- **`menu.py`**: Handles interactions with the application’s menu, including clicking buttons and taking screenshots.
- **`drive.py`**: Manages the train control logic, including reading distances, speeds, and speed limits.
- **`main.py`**: The entry point that starts the automation process and manages user input for starting and stopping the automation.

## Contribution

Contributions are welcome! Feel free to fork the repository and submit pull requests for improvements or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) for OCR capabilities.
- [OpenCV](https://opencv.org/) for image processing functionalities.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) for mouse and keyboard automation.
