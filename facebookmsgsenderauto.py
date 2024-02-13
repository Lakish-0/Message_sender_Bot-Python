#**************************************************************#
# this is module to automate 
import pyautogui
# this is time module 
import time

#for infinte loop
while True:
    #this write text
    pyautogui.typewrite('Hello')
    #this line stops code for 100 milisecond
    time.sleep(0.1)
    #this line enters text
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.typewrite('What are you doing?')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.typewrite('Testing python script!!')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(2)
#simple message bot
#********************************************************************#