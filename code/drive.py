import time
import pyautogui
import pytesseract
import keyboard  # For detecting key presses
from config import *  # Import all configurations

# Initialize throttle and brake levels
current_throttle = 0
current_brake = 0

def click_pixel(pixel_pos):
    pyautogui.click(pixel_pos)

def take_screenshot(portion, filename):
    screenshot = pyautogui.screenshot(region=portion)
    screenshot.save(filename)

def read_number(filename):
    image = pytesseract.image_to_string(filename)
    return int(image) if image.isdigit() else 0

def adjust_throttle(increment):
    global current_throttle
    if current_brake > 0:
        current_throttle = 0  # Set throttle to 0 if braking
    else:
        new_throttle = current_throttle + increment
        if 0 <= new_throttle <= MAX_THROTTLE:
            current_throttle = new_throttle
            print(f"Throttle level: {current_throttle}")

def adjust_brake(increment):
    global current_brake
    if current_throttle > 0:
        current_brake = 0  # Set brake to 0 when accelerating
    new_brake = current_brake + increment
    if 0 <= new_brake <= MAX_BRAKE:
        current_brake = new_brake
        print(f"Brake level: {current_brake}")

def control_train():
    global lastStation
    lastStation = 0

    click_pixel(AWSWarningPos)

    while True:
        time.sleep(1)
        click_pixel(AWSWarningPos)

        while True:
            # Capture and read distances and speeds
            take_screenshot(DistancePortion, "nextStationDist.png")
            NextStationDist = read_number("nextStationDist.png")
            NextStationDist = NextStationDist if NextStationDist > 0 else 0
            
            # Add TrainLength to the distance
            NextStationDist += TrainLength

            take_screenshot(CurrentSpeedPortion, "currentSpeed.png")
            CurrentSpeed = read_number("currentSpeed.png")

            take_screenshot(SpeedLimitPortion, "speedLimit.png")
            SpeedLimit = read_number("speedLimit.png")

            # Calculate stopping distance based on current speed and deceleration rate
            stopping_distance = (CurrentSpeed ** 2) / (2 * decelRate)

            # Automatic stopping logic
            if NextStationDist <= stopping_distance + 10:  # Start braking when close to stopping distance
                adjust_brake(1)  # Apply brakes gradually
                adjust_throttle(0)  # Ensure throttle is 0
            elif CurrentSpeed > SpeedLimit:  # If speeding
                adjust_brake(1)  # Apply brakes
            elif CurrentSpeed < SpeedLimit and current_brake == 0:
                adjust_throttle(1)  # Accelerate if below the speed limit

            # User control for throttle and brake
            if keyboard.is_pressed('w'):
                adjust_throttle(1)  # Increase throttle
                time.sleep(0.1)  # Delay to prevent rapid increments
            elif keyboard.is_pressed('s'):
                adjust_throttle(-1)  # Decrease throttle
                time.sleep(0.1)

            if keyboard.is_pressed('a'):
                adjust_brake(1)  # Increase brake
                adjust_throttle(0)  # Set throttle to 0 while braking
                time.sleep(0.1)
            elif keyboard.is_pressed('d'):
                adjust_brake(-1)  # Decrease brake
                time.sleep(0.1)

            # Check if the train has reached the station
            if NextStationDist <= 0 and CurrentSpeed == 0:
                time.sleep(1)  # Wait before trying to open doors
                pyautogui.press('t')  # Open doors
                break  # Exit the loop after opening doors

if __name__ == "__main__":
    control_train()
