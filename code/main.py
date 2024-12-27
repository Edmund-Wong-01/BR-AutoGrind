
import threading
import keyboard
from menu import main as start_menu
from drive import control_train

def run_program():
    while not stop_signal.is_set():
        start_menu()  # Start the menu functionality
        control_thread = threading.Thread(target=control_train)
        control_thread.start()

        # Wait for the control thread to finish
        control_thread.join()

def listen_for_stop():
    keyboard.wait('q')  # Wait for the user to press 'q' to stop
    stop_signal.set()  # Signal to stop the program

if __name__ == "__main__":
    stop_signal = threading.Event()  # Create a stop signal
    listener_thread = threading.Thread(target=listen_for_stop)
    listener_thread.start()  # Start the listener for the stop key

    run_program()  # Run the main program loop

    # Wait for the listener thread to finish
    listener_thread.join()
    print("Program stopped.")
