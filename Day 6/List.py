import os


#funtion to create list
list = []
minValue = 0
def createList():
    n = int(input("Enter the number of elements:"))
    for i in range(n):
        list.append(int(input("Enter the element {i+1}:")))

#funtion to display list
def displayList(list):
    for i in list:
        print(i, end=" ")

#function to add number
def addNumber(list):
    n = int(input("Enter the number to add:"))
    list.append(n)
#funtion ot remove number
def removeNumber(list):
    displayList(list)
    n = int(input("Enter the number to remove:"))
    list.remove(n)    

#function to display list of min to max
def minToMax(list):
    list.sort()  
    return list

def minAndMax(list):
    list.sort()
    minValue = list[0]
    maxValue = list[-1]
    return minValue, maxValue

#function to clear console
def clearConsole():
    os.system("cls")
createList()
#menu
while True:
    print("1. Add number")
    print("2. Remove number")
    print("3. Display list of min to max")
    print("4. Display min and max value")
    print("5. Exit")
    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            addNumber(list)
            clearConsole()
        case 2:
            removeNumber(list)
            clearConsole()
        case 3:
            print(minToMax(list))
            input("Press enter to continue...")
            clearConsole()
        case 4:
            print(minAndMax(list))
            input("Press enter to continue...")
            clearConsole()
        case 5:
            break
        case _:
            print("Invalid choice")
            break