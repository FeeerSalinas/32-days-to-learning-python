#librays
import random
import os

#array
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape","papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]

#var to stop the loop
found = False

#function to view the array with the words
def viewWords():
    print("The words are: ")
    for i in range(0, len(words)):
        print(words[i])
#function to clear console
def clearConsoel():
    os.system("cls")

#funtion to search the word
def searchWord(word):
    wordSearch = random.choice(words)  #random selects a word from the array
    if word == wordSearch:
        print("You guessed the word")
        found = True #stops the loop
    else:
        print("You did not guess the word")
        print("The word was: ", wordSearch)     
#loop to keep the game running
while found == False:
    viewWords()
    word = input("Enter a word: ")
    searchWord(word)
    input("Press enter to continue")
    clearConsoel()
