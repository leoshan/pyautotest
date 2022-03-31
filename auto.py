import pyautogui
import time
refreshx,refreshy = 112,50
closex,closey = 508,18
detailx,detaily = 1831,405
try:
    while True:
        pyautogui.click(refreshx,refreshy)
        time.sleep(2)
        pyautogui.click(detailx,detaily)
        time.sleep(2)
        buttonLocation = pyautogui.locateOnScreen('queding.png')
        if buttonLocation is not None:
            buttonx, buttony = pyautogui.center(buttonLocation)
            pyautogui.click(buttonx, buttony)
        time.sleep(2)
        pyautogui.click(closex,closey)
except KeyboardInterrupt:
    print('\nExit.')
