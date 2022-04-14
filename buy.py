import pyautogui
import time

#exe 60s
t_end = time.time() + 30
clickx,clicky = 1020,820
try:
    while time.time() < t_end:
        pyautogui.click(clickx,clicky)
except KeyboardInterrupt:
    print('\nExit.')
