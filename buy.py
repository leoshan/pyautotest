import pyautogui
import time

clickx,clicky = 1020,820
try:
    while True:
        pyautogui.click(clickx,clicky)
except KeyboardInterrupt:
    print('\nExit.')
