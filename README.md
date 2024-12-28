# BR AutoGrind
## Please do note that this project has not been tested. Use at your own risk.

## Foreword
This project is mostly AI generated, so please do expect some bugs and whatnot.

## Overview

This project automates British Railway, a Roblox train simulation game. 
## Features

- Finds the most optimal route. (points per minute)
- Sticks to speed limit.
- Acknowledge AWS Warnings.
- Open and close doors.
- Can move forward if train is not fully in station.
- Utilizes analog brake and throttle.

## Caveats 
- It does NOT have guard capabilities.
- It does NOT obey danger aspects. Therefore it only works on **PRIVATE SERVERS**
- It does NOT stop at car markers, however it  will nudge forward if the train's not fully in the platform.
- It does NOT know what to do when Roblox crashes.

## To-do 
- Stop at markers

## Settings in BR
- Set to seperate throttle and brake

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

Ensure you have `pip` installed, then run this command:

```bash
pip install pyautogui
pip install pytesseract
pip install keyboard
pip install Pillow
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

In `drive.py` and `menu.py`, add the following line:

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
