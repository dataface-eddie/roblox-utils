import time
import pyautogui
from pynput import keyboard

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

click_locations = []
start_replay = False
stop_all = False

print("Move mouse to where you want to click, then press Z to record that point.")
print("Press X to start replaying clicks (3s between).")
print("Press ESC to quit. (Also: move mouse to top-left for PyAutoGUI failsafe.)")

def on_press(key):
    global start_replay, stop_all

    try:
        if key.char in ('z', 'Z'):
            x, y = pyautogui.position()
            click_locations.append((x, y))
            print(f"Added click location #{len(click_locations)}: ({x}, {y})")

        elif key.char in ('x', 'X'):
            if not click_locations:
                print("No click locations recorded yet.")
            else:
                start_replay = True
                print("Starting replay...")

    except AttributeError:
        # Special keys (like ESC) land here
        if key == keyboard.Key.esc:
            stop_all = True
            print("Stopping.")
            return False  # stop listener

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    # Main loop
    while not stop_all:
        if start_replay:
            # Replay through the list until user stops
            while True:
                for (x, y) in click_locations:
                    pyautogui.click(x, y)
                    print(f"Clicked at: ({x}, {y})")
                    time.sleep(3.1)  # wait 3 seconds between clicks

                print("Finished replay.")
                start_replay = False  # allow starting again with X

        time.sleep(0.05)

except pyautogui.FailSafeException:
    print("Stopped safely via FAILSAFE (top-left corner).")
finally:
    stop_all = True