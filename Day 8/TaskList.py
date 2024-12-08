import os

#list
task = []
#function to add task
def addTask(list):
    task = input("Enter the task to add: ")
    list.append(task)   
#function to show task
def showTask(list):
    if len(list) == 0:
        print("No task to show")
    for i in list:
        print(i)
#function to remove task
def removeTask(list):
    showTask(list)
    task = input("Enter the task to remove: ")
    list.remove(task)

#main menu
while True:
    print("1. Add Task")
    print("2. Show Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            addTask(task)
            os.system("cls")
        case 2:
            showTask(task)
            input("Press enter to continue...")
            os.system("cls")
        case 3:
            removeTask(task)
            os.system("cls")
        case 4:
            break
        case _:
            print("Invalid choice")
            break