import time
import pyautogui
import pytesseract
from config import *

def click_pixel(pixel_pos):
    pyautogui.click(pixel_pos)

def take_screenshot(portion, filename):
    screenshot = pyautogui.screenshot(region=portion)
    screenshot.save(filename)

def read_number(filename):
    image = pytesseract.image_to_string(filename)
    return int(image) if image.isdigit() else 0

def screen_matches(target_image_path, region):
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("temp_screenshot.png")
    return pyautogui.locateOnScreen(target_image_path, confidence=0.8) is not None

def control_train():
    global lastStation
    lastStation = 0

    while True:
        click_pixel(AWSWarningPos)
        take_screenshot(DistancePortion, "nextStationDist.png")
        
        # Read distance; default to 0 if OCR fails
        NextStationDist = read_number("nextStationDist.png")
        NextStationDist = NextStationDist if NextStationDist > 0 else 0
        
        # Add TrainLength to the distance
        NextStationDist += TrainLength  # Adjust for train length

        take_screenshot(CurrentSpeedPortion, "currentSpeed.png")
        CurrentSpeed = read_number("currentSpeed.png")

        take_screenshot(SpeedLimitPortion, "speedLimit.png")
        SpeedLimit = read_number("speedLimit.png")

        # Train control logic
        while NextStationDist > 0:
            if CurrentSpeed < SpeedLimit:
                pyautogui.keyDown('w')
                time.sleep(0.1)  # Delay for acceleration
            elif CurrentSpeed > SpeedLimit:
                pyautogui.keyDown('s')
                time.sleep(0.1)

            # Update screenshots and values
            take_screenshot(DistancePortion, "nextStationDist.png")
            NextStationDist = read_number("nextStationDist.png")
            NextStationDist = NextStationDist if NextStationDist > 0 else 0  # Default to 0 if OCR fails
            NextStationDist += TrainLength  # Adjust for train length
        
        pyautogui.press('t')  # Open doors
        take_screenshot("openDoor.png")

        if "Your train must be fully in a station to open doors" in pytesseract.image_to_string("openDoor.png"):
            pyautogui.keyDown('w')
            time.sleep(creepForwardFromBrakeSec)
            while "Your train must be fully in a station to open doors" in pytesseract.image_to_string("openDoor.png"):
                pyautogui.press('t')
                take_screenshot("notFullyInStation.png")

        if lastStation == 0:
            while "loading complete" not in pytesseract.image_to_string("checkForCloseDoors.png"):
                take_screenshot("checkForCloseDoors.png")

        # Check for the specific condition to set lastStation
        if screen_matches("target_image.png", (x, y, width, height)):  # Replace with actual values
            lastStation = 1
            break  # Exit the loop once condition is met

if __name__ == "__main__":
    control_train()
