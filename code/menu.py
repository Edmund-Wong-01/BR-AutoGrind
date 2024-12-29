import time
import pyautogui
import pytesseract
import re
from config import *

def clickOnPixel(position):
    """Click on a specified pixel position."""
    pyautogui.click(position[0], position[1])
    time.sleep(sleepTime)

def takeScreenshot(region):
    """Take a screenshot of a specified region."""
    return pyautogui.screenshot(region=region)

def findMinsCount(screenshot):
    """Count occurrences of the word 'mins' in the screenshot."""
    text = pytesseract.image_to_string(screenshot)
    return len(re.findall(r'\bmins\b', text, re.IGNORECASE))

def extractNumbersFromImage(screenshot):
    """Extract all numbers from the screenshot."""
    text = pytesseract.image_to_string(screenshot)
    return [int(num) for num in re.findall(r'\d+', text)]

def calculateRatios(leftNumbers, rightNumbers):
    """Calculate the ratio of right numbers to left numbers."""
    ratios = []
    for left, right in zip(leftNumbers, rightNumbers):
        if left != 0:
            ratios.append(right / left)
        else:
            ratios.append(0)  # Handle division by zero
    return ratios

def main():
    # Click on initial positions
    clickOnPixel(drivePos)
    clickOnPixel(loadConsistPos)
    clickOnPixel(consistPos)
    clickOnPixel(continuePos)

    # Step 1: Take a screenshot of destinations
    destinationScreenshot = takeScreenshot(destinationPortion)

    # Step 2: Find the count of "mins"
    minsCount = findMinsCount(destinationScreenshot)

    # Get the position of each "mins"
    minsPositions = []
    for i in range(minsCount):
        minsPositions.append((destinationPortion[0], destinationPortion[1] + i * minsSpacing))

    highestRatios = []

    for pos in minsPositions:
        # Step 3: Click on the current position of "mins"
        pyautogui.click(pos[0], pos[1])
        time.sleep(sleepTime)

        # Step 4: Take a screenshot of routes
        routeScreenshot = takeScreenshot(routePortion)

        # Step 5: Extract numbers from the screenshot
        numbers = extractNumbersFromImage(routeScreenshot)

        # Separate into left and right numbers
        leftNumbers = numbers[0::2]  # Left numbers at even indices
        rightNumbers = numbers[1::2]  # Right numbers at odd indices

        # Step 6: Calculate ratios
        ratios = calculateRatios(leftNumbers, rightNumbers)

        # Step 7: Track highest ratio and its position
        if ratios:
            maxRatio = max(ratios)
            maxIndex = ratios.index(maxRatio)
            highestRatios.append((maxRatio, maxIndex))

        time.sleep(sleepTime)  # Wait before the next iteration

    # Click on destination with the highest ratio
    if highestRatios:
        highestDestIndex = highestRatios.index(max(highestRatios, key=lambda x: x[0]))
        # Click logic to select destination can be added here
        print(f"Clicking on destination with highest ratio at index: {highestDestIndex}")

        # Click on route with highest ratio
        highestRouteIndex = highestRatios[highestDestIndex][1]
        # Click logic to select route can be added here
        print(f"Clicking on route with highest ratio at index: {highestRouteIndex}")

    # Step to click on continuePos
    clickOnPixel(continuePos)

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
