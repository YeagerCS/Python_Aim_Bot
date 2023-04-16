# Python_Aim_Bot


## What is it
The script.py script, is a script that works for the website https://aim400kg.com/game/1. It functions for the given game and clicks the targets that appear, just as you would normally do. Although the accuracy isn't 100%, it clicks targets quite quickly, and the ratings it receives are still much higher than what humans can achieve.

## How does it work
It works by taking a screenshot of the region in which your game is open and then locating the rgb of the target. Once it finds the correct color, it will move the mouse at that position and click it. For the specified website, it was best to check the range of the red color and clicking when the red color is inbetween the range of 93 and 99. To improve accuracy, the red value 97 is not included, because dot that pops up when missing the targets has exactly the value 97 on red.

## How to use it
Additionally to the script.py file, there is the regionCalc.py file. The regionCalc file helps you find out the screenshot region for your game. After you started the regionCalc program, you need to go to your window in which the game is at and then clicking 'a' in the topleft corner, and 'b' in the topright corner. With those two coordinates, the program will calculate the region and will print out the output of the region. This output is to be stored in the ```screenshotRegion``` variable. After doing that, the program should work.

If you want to try it at another website, instead of https://aim400kg.com/game/1, you just have to locate the color of the element that it is clicking. You can do this with the python shell by using the ``` pyautogui.displayMousePosition() ``` command.

## Imports

``` pip install pyautogui ```
``` pip install keyboard ``` 
``` pip install pynput.mouse ```
