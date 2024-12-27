import time
import pyautogui
import pytesseract
from config import *

def click_pixel(pixel_pos):
    pyautogui.click(pixel_pos)

def take_screenshot(portion, filename):
    screenshot = pyautogui.screenshot(region=portion)
    screenshot.save(filename)

def find_numbers(image):
    text = pytesseract.image_to_string(image)
    return [int(num) for num in text.split() if num.isdigit()]

def calculate_ratios(left, right):
    return right / left if left else 0

def main():
    click_pixel(DrivePos)
    click_pixel(LoadConsistPos)
    click_pixel(ConsistPos)
    click_pixel(ContinuePos)

    take_screenshot(MainRoutePortion, "mainRoute.png")
    numbers = find_numbers("mainRoute.png")

    # Assume numbers are in pairs (left, right)
    ratios = [calculate_ratios(numbers[i], numbers[i+1]) for i in range(0, len(numbers), 2)]
    max_index = ratios.index(max(ratios))

    click_pixel(SecondaryRoutePortion[max_index])  # Click on the highest ratio
    take_screenshot(SecondaryRoutePortion, "secondaryRoute.png")

    # Repeat number finding and clicking
    numbers_secondary = find_numbers("secondaryRoute.png")
    click_pixel(SecondaryRoutePortion[numbers_secondary.index(max(numbers_secondary))])
    click_pixel(ContinuePos)

    # Wait for throttle red position
    while True:
        r, g, b = pyautogui.pixel(*ThrottleRedPos)
        if all(abs(c - throttleRedRGB) <= RGB_TOLERANCE for c in (r, g, b)):
            break

    # Press keys
    pyautogui.press("p")
    pyautogui.press("{")

if __name__ == "__main__":
    main()
