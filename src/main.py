import cv2 as cv
import numpy as np
from pynput import mouse, keyboard
import threading
import time
 
cap = cv.VideoCapture(1)
idle_threshold = 1
last_activity_time = time.time()
phone_in_frame = False

def scream() -> None:
    print("lock in")
    #replace with the serial call to the unpleasantries
    return 

def check_for_inactivity():
    global last_activity_time
    # Check for the lack of inputs after idle_threshold
    while(True):
        if time.time() - last_activity_time > idle_threshold:
            print(f"No input detected for {idle_threshold} seconds. Performing idle action...")

            if(True): #replace magic Truth with phone_in_frame once implemented
                scream()

            last_activity_time = time.time() # Reset to avoid repeated messages
            time.sleep(1) # Check every second

def on_input(*args):
    """Callback for any keyboard or mouse event."""
    global last_activity_time
    last_activity_time = time.time()

def camera_loop():
    global cap
    global phone_in_frame
    while True:
        ret, frame = cap.read()
        # 'ret' is a boolean indicating if the frame was read successfully
        # 'frame' is the actual image (NumPy array) captured from the webcam

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # check for phone here
        
        # Display the frame (original or processed)
        cv.imshow('Webcam Feed', frame)

        # Exit the loop when 'q' is pressed
        if cv.waitKey(1) == ord('q'):
            break

keyboard_listener = keyboard.Listener(on_press=on_input, on_release=on_input)
mouse_listener = mouse.Listener(on_click=on_input, on_move=on_input, on_scroll=on_input)

keyboard_listener.start()
mouse_listener.start()

inactivity_checker = threading.Thread(target=check_for_inactivity)
inactivity_checker.daemon = True  # Allows the main program to exit without waiting for this thread
inactivity_checker.start()

main_loop = threading.Thread(target=camera_loop)
main_loop.daemon = True
main_loop.start()
main_loop.join()
inactivity_checker.join()





    
