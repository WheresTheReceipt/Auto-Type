import pyautogui
import time
import random

try:
    enter = int(input('Enter the amount of time you want the bot to type the command: '))
except ValueError:
    print('Must be a Number.')


times = 0
print('Starting Program you have 5 seconds.')
time.sleep(5)
Entercommand = random.randint(15, 26)
while times < enter:
    pyautogui.typewrite('.work')
    pyautogui.press('enter')
    times += 1
    time.sleep(random.randint(15, 47))

print(times)
