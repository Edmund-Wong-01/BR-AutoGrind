import time
import pyautogui
import pytesseract
from config import *  # Import all configurations

# Define throttle and brake levels
throttleSteps = 7  # Steps from OFF (0) to FULL (6)
brakeSteps = 4     # Steps from OFF (0) to MAX (4)

# Initialize throttle and brake levels
throttleLevel = 0
brakeLevel = 4
lastStation = 0  # Initialize lastStation

def clickPixel(pixelPos):
    pyautogui.click(pixelPos)

def takeScreenshot(portion, filename):
    screenshot = pyautogui.screenshot(region=portion)
    screenshot.save(filename)

def readNumber(filename):
    image = pytesseract.image_to_string(filename)
    return int(image) if image.isdigit() else 0

def calculateBrakingDistance(currentSpeed):
    # Calculate the distance needed to stop based on deceleration rate
    return (currentSpeed ** 2) / (2 * decelRate)

def controlTrain():
    global lastStation

    # Initial click to acknowledge AWS warning
    clickPixel(AWSWarningPos)

    # Main control loop
    while lastStation == 0:  # Repeat until lastStation is set to 1
        # Click the AWS warning every second if it exists
        time.sleep(1)
        clickPixel(AWSWarningPos)

        takeScreenshot(distancePortion, "nextStationDist.png")
        nextStationDist = readNumber("nextStationDist.png")
        nextStationDist = max(0, nextStationDist + trainLength)  # Adjust for train length

        takeScreenshot(currentSpeedPortion, "currentSpeed.png")
        currentSpeed = readNumber("currentSpeed.png")

        takeScreenshot(speedLimitPortion, "speedLimit.png")
        speedLimit = readNumber("speedLimit.png")

        # Control loop for throttle and brake
        while nextStationDist > 0:
            # Apply full throttle when trying to reach speed limit
            if currentSpeed < speedLimit:
                throttleLevel = throttleSteps - 1  # Set to full throttle
                pyautogui.keyDown('w')  # Apply throttle
                time.sleep(0.1 * throttleLevel)  # Adjust acceleration duration
            else:
                pyautogui.keyUp('w')  # No throttle applied

            # Calculate the required braking distance
            brakingDistance = calculateBrakingDistance(currentSpeed)

            # If approaching station, apply brakes based on distance
            if nextStationDist < brakingDistance + 100:  # 100m buffer; adjust as necessary
                if brakeLevel < brakeSteps - 1:
                    time.sleep(1)  # Wait 1 second before going to max brake
                    brakeLevel = brakeSteps - 1  # Set to max brake
                pyautogui.keyDown('s')  # Apply brake
                time.sleep(0.1 * brakeLevel)  # Adjust braking duration
            else:
                pyautogui.keyUp('s')  # No brake applied

            # Update distance
            takeScreenshot(distancePortion, "nextStationDist.png")
            nextStationDist = readNumber("nextStationDist.png")
            nextStationDist = max(0, nextStationDist + trainLength)  # Adjust for train length

        # Wait for a second before pressing 't' to open doors
        time.sleep(1)
        pyautogui.press('t')  # Attempt to open doors
        takeScreenshot("openDoor.png")

        # Check if the train is fully in the station
        while True:
            takeScreenshot("openDoor.png")
            doorStatus = pytesseract.image_to_string("openDoor.png")

            if "You must be stopped to open doors." in doorStatus:
                break  # Exit the loop if the condition is met

            # If not fully in station, continue moving slightly forward
            pyautogui.keyDown('w')  # Move forward
            time.sleep(creepForwardFromBrakeSec)

        # Once the train is completely in the station, hold 's' for 1 second
        time.sleep(1)
        pyautogui.keyDown('s')  # Hold 's' to decelerate
        time.sleep(1)  # Hold for another second
        pyautogui.keyUp('s')  # Release 's'

        # Wait for a second before pressing 't' to open doors
        time.sleep(1)
        pyautogui.press('t')  # Attempt to open doors

        # Handle the case when loading is complete
        if lastStation == 0:
            # Wait for a second before checking for loading complete
            time.sleep(1)
            while "loading complete" not in pytesseract.image_to_string("checkForCloseDoors.png"):
                takeScreenshot("checkForCloseDoors.png")

        # Check for specific condition to set lastStation
        if screen_matches("target_image.png", (x, y, width, height)):  # Replace with actual values
            lastStation = 1  # Set lastStation to 1 to exit the loop
            break  # Exit the loop to end the control process

        # Control input for throttle and brake (this section should be checked in an appropriate context)
        if pyautogui.keyDown('w') and throttleLevel < throttleSteps - 1:
            throttleLevel += 1  # Increase throttle level
        if pyautogui.keyDown('s') and throttleLevel > 0:
            throttleLevel -= 1  # Decrease throttle level
        if pyautogui.keyDown('a') and brakeLevel < brakeSteps - 1:
            brakeLevel += 1  # Increase brake level
        if pyautogui.keyDown('d') and brakeLevel > 0:
            brakeLevel -= 1  # Decrease brake level

if __name__ == "__main__":
    controlTrain()
