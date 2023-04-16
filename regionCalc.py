import keyboard
from pynput.mouse import Controller

mouse = Controller()

(x, y, width, height) = (0, 0, 0, 0)
while True:
    if keyboard.is_pressed('a'):
        (x, y) = mouse.position
        break

(x2, y2) = (0, 0)

while True:
    if keyboard.is_pressed('b'):
        (x2, y2) = mouse.position
        break

(width, height) = (x2 - x, y2 - y)

print(f"x: {x}, y: {y}, width: {width}, height: {height}")
print(f"({x}, {y}, {width}, {height})")