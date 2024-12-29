import threading
import keyboard
from menu import main as startMenu
from drive import controlTrain

def runProgram():
    while not stopSignal.is_set():
        startMenu()  # Start the menu functionality
        controlThread = threading.Thread(target=controlTrain)
        controlThread.start()

        # Wait for the control thread to finish
        controlThread.join()

def listenForStop():
    keyboard.wait('q')  # Wait for the user to press 'q' to stop
    stopSignal.set()  # Signal to stop the program

if __name__ == "__main__":
    stopSignal = threading.Event()  # Create a stop signal
    listenerThread = threading.Thread(target=listenForStop)
    listenerThread.start()  # Start the listener for the stop key

    runProgram()  # Run the main program loop

    # Wait for the listener thread to finish
    listenerThread.join()
    print("Program stopped.")
