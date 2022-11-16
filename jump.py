import pyautogui as py
import time

currentMouseX, currentMouseY = py.position()

while True:
    time.sleep(3)
    py.press('esc')
    time.sleep(2)
    py.click(1537, 936)
    time.sleep(3)
    py.click(2515, 763)
    time.sleep(2)
    py.click(2436, 962)
    time.sleep(1320)