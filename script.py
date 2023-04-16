import pyautogui
from pynput.mouse import Controller, Button
import time
import keyboard

time.sleep(2)

rgb = (93, 108, 134)
rgb = (97, 108, 134)
screenshotRegion = (432, 258, 1053, 629)

mouse = Controller()

def click(x, y):
    mouse.position = (x, y)
    mouse.press(Button.left)
    mouse.release(Button.left)


while not keyboard.is_pressed('q'):
    screenshot = pyautogui.screenshot(region=screenshotRegion)
    (width, height) = screenshot.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            (r, g, b) = screenshot.getpixel((x, y))
            if r in range(93, 99) and r != 97:
                click(x+432, y+258)
                time.sleep(0.07)
                break
