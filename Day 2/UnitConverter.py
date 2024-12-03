#librarys 
import os 


#function to convert length
def convertLength(optionLength):
    if optionLength == 1:
        cm = float(input("Enter the length in cm: "))
        m = cm/100
        return f"{cm} cm is {m} m"
    elif optionLength == 2:
        m = float(input("Enter the lenth in m: "))
        km = m/100
        return f"{m} m is {km} km"
    
#function to convert temp
def convertTemp(optionTemp):
    if optionTemp == 1:
        c = float(input("Enter the temp in C: "))
        k = c + 273.15
        return f"{c} C is {k} K"
    elif optionTemp == 2:
        c = float(input("Enter the temp in C: "))
        f = (c * 9/5) + 32
        return f"{c} C is {f} F"

#function to convert time
def convertTime(optionTime):
    if optionTime == 1:
        s = float(input("Enter the time in seconds: "))
        m = s/60
        return f"{s} second is {m} minutes"
    elif optionTime == 2:
        m = float(input("Enter the time in minutes: "))
        h = m/60;
        return f"{m} minutes is {h} hours"
#function to clear console
def clearConsole():
    os.system("cls")

#main menu
while True:
    clearConsole()
    print("1-Convert length")
    print("2-Convert temp")
    print("3-Convert time")
    print("4-Exit")
    option = int(input("Choose a option: "))
    #option 1 to convert length
    if option == 1:
        print("1-Convert cm to m")
        print("2-Convert m to km")
        optionLength = int(input("Choose a option: "))
        result = convertLength(optionLength)
        print(result)
        input("Press enter to continue...")
    #option 2 to convert temp
    elif option == 2:
        print("1-Convert Celcius to Kelvins")
        print("2-Convert Celcius to Farenhein")
        optionTemp = int(input("Choose a option: "))
        result = convertTemp(optionTemp)
        print(result)
        input("Press enter to continue...")
    #option 3 to convert time
    elif option == 3:
        print("1-Convert second to minutes ")
        print("2-Convert minutes to hours")
        optionTime = int(input("Choose the opcion: "))
        result = convertTime(optionTime)
        print(result)
        input("Press enter to continue...")
    elif option == 4:
        break