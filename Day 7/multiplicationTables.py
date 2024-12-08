import os

#function to show multiplication table

def showTable():
    num = int(input("Enter the number to show table: "))
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")


#main menu
while True:
    print("1. Show Table")
    print("2. Exit")
    choice = int(input("Enter your choice:"))

    match choice:
        case 1:
            showTable()
            input("Press enter to continue...")
            os.system("cls")
        case 2:
            break
        case _:
            print("Invalid choice")
            break
