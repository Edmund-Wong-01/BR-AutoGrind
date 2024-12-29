import time
import pyautogui
import pytesseract
import re
from config import DESTINATION_PORTION, ROUTE_PORTION, MINS_SPACING, SLEEP_TIME

def click_on_pixel(position):
    """Click on a specified pixel position."""
    pyautogui.click(position[0], position[1])
    time.sleep(SLEEP_TIME)

def take_screenshot(region):
    """Take a screenshot of a specified region."""
    return pyautogui.screenshot(region=region)

def find_mins_count(screenshot):
    """Count occurrences of the word 'mins' in the screenshot."""
    text = pytesseract.image_to_string(screenshot)
    return len(re.findall(r'\bmins\b', text, re.IGNORECASE))

def extract_numbers_from_image(screenshot):
    """Extract all numbers from the screenshot."""
    text = pytesseract.image_to_string(screenshot)
    return [int(num) for num in re.findall(r'\d+', text)]

def calculate_ratios(left_numbers, right_numbers):
    """Calculate the ratio of right numbers to left numbers."""
    ratios = []
    for left, right in zip(left_numbers, right_numbers):
        if left != 0:
            ratios.append(right / left)
        else:
            ratios.append(0)  # Handle division by zero
    return ratios

def main():
    # Click on initial positions
    click_on_pixel(drivePos)
    click_on_pixel(loadConsistPos)
    click_on_pixel(consistPos)
    click_on_pixel(continuePos)

    # Step 1: Take a screenshot of destinations
    destination_screenshot = take_screenshot(DESTINATION_PORTION)

    # Step 2: Find the count of "mins"
    mins_count = find_mins_count(destination_screenshot)

    # Get the position of each "mins"
    mins_positions = []
    for i in range(mins_count):
        mins_positions.append((DESTINATION_PORTION[0], DESTINATION_PORTION[1] + i * MINS_SPACING))

    highest_ratios = []

    for pos in mins_positions:
        # Step 3: Click on the current position of "mins"
        pyautogui.click(pos[0], pos[1])
        time.sleep(SLEEP_TIME)

        # Step 4: Take a screenshot of routes
        route_screenshot = take_screenshot(ROUTE_PORTION)

        # Step 5: Extract numbers from the screenshot
        numbers = extract_numbers_from_image(route_screenshot)

        # Separate into left and right numbers
        left_numbers = numbers[0::2]  # Left numbers at even indices
        right_numbers = numbers[1::2]  # Right numbers at odd indices

        # Step 6: Calculate ratios
        ratios = calculate_ratios(left_numbers, right_numbers)

        # Step 7: Track highest ratio and its position
        if ratios:
            max_ratio = max(ratios)
            max_index = ratios.index(max_ratio)
            highest_ratios.append((max_ratio, max_index))

        time.sleep(SLEEP_TIME)  # Wait before the next iteration

    # Click on destination with the highest ratio
    if highest_ratios:
        highest_dest_index = highest_ratios.index(max(highest_ratios, key=lambda x: x[0]))
        # Click logic to select destination can be added here
        print(f"Clicking on destination with highest ratio at index: {highest_dest_index}")

        # Click on route with highest ratio
        highest_route_index = highest_ratios[highest_dest_index][1]
        # Click logic to select route can be added here
        print(f"Clicking on route with highest ratio at index: {highest_route_index}")

    # Step to click on continueDrivePos
    click_on_pixel(continuePos)

    # Wait until pixel throttleRedPos has the specified RGB value
    while True:
        color = pyautogui.pixel(throttleRedPos[0], throttleRedPos[1])
        if color == throttleRedRGB:
            break
        time.sleep(0.5)  # Poll every half second

    # Press the keys "p" and "{"
    pyautogui.press('p')
    pyautogui.press('{')

if __name__ == "__main__":
    main()
