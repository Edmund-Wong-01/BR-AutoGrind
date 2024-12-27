import keyboard  # Make sure to install the keyboard library
import time
from menu import main_menu
from drive import train_control

running = False

def start_process():
    global running
    running = True
    while running:
        main_menu()
        train_control()

def stop_process():
    global running
    running = False

keyboard.add_hotkey('s', start_process)
keyboard.add_hotkey('e', stop_process)

# Keep the program running
while True:
    time.sleep(1)
