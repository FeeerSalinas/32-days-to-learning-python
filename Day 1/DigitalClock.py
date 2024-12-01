#definitiion of librarys
from time import localtime, strftime, sleep
import os
#function to clear the console
def clearConsole():
    os.system("cls")
#function to print the actual time
def digitalClock():
    while True:
        print(strftime("Time: %H:%M:%S", localtime()))
        sleep(1) #the loop run every second
        clearConsole()
#call the function
digitalClock()