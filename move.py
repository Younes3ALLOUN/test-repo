import pyautogui
import time
import random

def move_mouse():
    # Get the screen size
    screen_width, screen_height = pyautogui.size()

    # Generate random coordinates within the screen bounds
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)

    # Move the mouse to the generated coordinates
    pyautogui.moveTo(x, y, duration=0.3)

# Set the interval in seconds
interval = 10  # 2 minutes

try:
    while True:
        move_mouse()
        time.sleep(interval)
except KeyboardInterrupt:
    print("Script interrupted.")
