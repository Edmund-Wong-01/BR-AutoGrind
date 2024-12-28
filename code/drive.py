import time
import pyautogui
import pytesseract
from config import *  # Import all configurations

# Define throttle and brake levels
THROTTLE_STEPS = 7  # Steps from OFF (0) to FULL (6)
BRAKE_STEPS = 5     # Steps from OFF (0) to MAX (4)

# Initialize throttle and brake levels
throttle_level = 0
brake_level = 4
lastStation = 0  # Initialize lastStation

def click_pixel(pixel_pos):
    pyautogui.click(pixel_pos)

def take_screenshot(portion, filename):
    screenshot = pyautogui.screenshot(region=portion)
    screenshot.save(filename)

def read_number(filename):
    image = pytesseract.image_to_string(filename)
    return int(image) if image.isdigit() else 0

def calculate_braking_distance(current_speed):
    # Calculate the distance needed to stop based on deceleration rate
    return (current_speed ** 2) / (2 * decelRate)

def control_train():
    global lastStation

    # Initial click to acknowledge AWS warning
    click_pixel(AWSWarningPos)

    # Main control loop
    while lastStation == 0:  # Repeat until lastStation is set to 1
        # Click the AWS warning every second if it exists
        time.sleep(1)
        click_pixel(AWSWarningPos)

        take_screenshot(DistancePortion, "nextStationDist.png")
        NextStationDist = read_number("nextStationDist.png")
        NextStationDist = max(0, NextStationDist + TrainLength)  # Adjust for train length

        take_screenshot(CurrentSpeedPortion, "currentSpeed.png")
        CurrentSpeed = read_number("currentSpeed.png")

        take_screenshot(SpeedLimitPortion, "speedLimit.png")
        SpeedLimit = read_number("speedLimit.png")

        # Control loop for throttle and brake
        while NextStationDist > 0:
            # Apply full throttle when trying to reach speed limit
            if CurrentSpeed < SpeedLimit:
                throttle_level = THROTTLE_STEPS - 1  # Set to full throttle
                pyautogui.keyDown('w')  # Apply throttle
                time.sleep(0.1 * throttle_level)  # Adjust acceleration duration
            else:
                pyautogui.keyUp('w')  # No throttle applied

            # Calculate the required braking distance
            braking_distance = calculate_braking_distance(CurrentSpeed)

            # If approaching station, apply brakes based on distance
            if NextStationDist < braking_distance + 100:  # 100m buffer; adjust as necessary
                if brake_level < BRAKE_STEPS - 1:
                    time.sleep(1)  # Wait 1 second before going to max brake
                    brake_level = BRAKE_STEPS - 1  # Set to max brake
                pyautogui.keyDown('s')  # Apply brake
                time.sleep(0.1 * brake_level)  # Adjust braking duration
            else:
                pyautogui.keyUp('s')  # No brake applied

            # Update distance
            take_screenshot(DistancePortion, "nextStationDist.png")
            NextStationDist = read_number("nextStationDist.png")
            NextStationDist = max(0, NextStationDist + TrainLength)  # Adjust for train length

        # Wait for a second before pressing 't' to open doors
        time.sleep(1)
        pyautogui.press('t')  # Attempt to open doors
        take_screenshot("openDoor.png")

        # Check if the train is fully in the station
        while True:
            take_screenshot("openDoor.png")
            door_status = pytesseract.image_to_string("openDoor.png")

            if "You must be stopped to open doors." in door_status:
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
                take_screenshot("checkForCloseDoors.png")

        # Check for specific condition to set lastStation
        if screen_matches("target_image.png", (x, y, width, height)):  # Replace with actual values
            lastStation = 1  # Set lastStation to 1 to exit the loop
            break  # Exit the loop to end the control process

        # Control input for throttle and brake (this section should be checked in an appropriate context)
        if pyautogui.keyDown('w') and throttle_level < THROTTLE_STEPS - 1:
            throttle_level += 1  # Increase throttle level
        if pyautogui.keyDown('s') and throttle_level > 0:
            throttle_level -= 1  # Decrease throttle level
        if pyautogui.keyDown('a') and brake_level < BRAKE_STEPS - 1:
            brake_level += 1  # Increase brake level
        if pyautogui.keyDown('d') and brake_level > 0:
            brake_level -= 1  # Decrease brake level

if __name__ == "__main__":
    control_train()
