import pyautogui
import time
import random

#This makes sure the user enters a Number
try:
    enter = int(input('Enter the amount of time you want the bot to type the command: '))
except ValueError:
    print('Must be a Number.')


times = 0
print('Starting Program you have 5 seconds.')
time.sleep(5)
Entercommand = random.randint(15, 26)
while times < enter:
    pyautogui.typewrite('CHANGE ME')     #This is where you type the message you want
    pyautogui.press('enter')       #This automatically clicks your enter key
    times += 1
    
    #You have 2 option here based on your circumstances. Uncomment Only One of them.
    
    #time.sleep(random.randint(15, 47))    #You can change these if you want. This is the random time it will take to send the command.
    #time.sleep(1)               #This line if you want the bot to send the message every second.

    print(times)                #Prints how many times the bot typed in the Word/Command
