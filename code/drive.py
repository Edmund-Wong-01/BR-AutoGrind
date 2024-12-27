import time
import cv2
import pytesseract
import pyautogui
from config import *

def take_screenshot(filename, portion):
    # Function to take a screenshot and save it
    # Implement using pyautogui or similar library
    pass

def read_distance():
    image = take_screenshot("nextStationDist.png", distancePortion)
    text = pytesseract.image_to_string(image, config='outputbase digits')
    return int(text) if text.isdigit() else 0

def read_current_speed():
    image = take_screenshot("currentSpeed.png", currentSpeedPortion)
    text = pytesseract.image_to_string(image, config='outputbase digits')
    return int(text) if text.isdigit() else 0

def read_speed_limit():
    image = take_screenshot("speedLimit.png", speedLimitPortion)
    text = pytesseract.image_to_string(image, config='outputbase digits')
    return int(text) if text.isdigit() else 0

def click_aws_warning():
    # Click on the AWSWarningPos every second
    while True:
        pyautogui.click(AWSWarningPos)  # Click on the defined position
        time.sleep(1)  # Wait for 1 second

def train_control():
    # Start a separate thread for clicking AWSWarningPos
    import threading
    aws_thread = threading.Thread(target=click_aws_warning)
    aws_thread.daemon = True  # Daemonize thread
    aws_thread.start()

    while True:
        nextStationDist = read_distance()
        if nextStationDist == 0:
            break

        currentSpeed = read_current_speed()
        speedLimit = read_speed_limit()

        # Implement train control logic here

    # After stopping
    take_screenshot("openDoor.png", (0, 0, 100, 100))
    # Check and handle door opening condition
