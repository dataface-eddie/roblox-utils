import pyautogui
import time
import random

pyautogui.FAILSAFE = True     # Move mouse to top-left corner to STOP
pyautogui.PAUSE = 0.01

print("Auto-clicking.")
print("🚨 EMERGENCY STOP: Move mouse to TOP-LEFT corner")

try:
    while True:
        pyautogui.click()

        # move mouse slightly at random (-20 to +20 pixels)
        dx = random.randint(-20, 20)
        dy = random.randint(-20, 20)
        pyautogui.moveRel(dx, dy)

        time.sleep(1)# wait 1 second between clicks
        #reset mouse position to center of screen
        screenWidth, screenHeight = pyautogui.size()
        pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
except pyautogui.FailSafeException:
    print("Stopped safely.")