#import library
import os


#function to encrypt the text
def Ciphey():
    #taking input from user
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    #empty string to store the encrypted text
    cipher = ""
    #loop through each character in the text
    for char in text:
        #if the character is a letter
        if char.isalpha():
            #get the unicode of the character
            unicode = ord(char)
            #if the character is uppercase
            if char.isupper(): 
                #shift the character by the shift value
                unicode = (unicode + shift - 65) % 26 + 65
            #if the character is lowercase
            else:
                #shift the character by the shift value
                unicode = (unicode + shift - 97) % 26 + 97
            #add the character to the encrypted text
            cipher += chr(unicode)
        #if the character is not a letter
        else:
            #add the character to the encrypted text
            cipher += char
    #print the encrypted text
    print("The encrypted text is:", cipher)
    #ask the user if they want to decrypt the text
    decrypt = input("Do you want to decrypt the text? (y/n): ")
    #if the user wants to decrypt the text
    if decrypt == "y":
        #call the decrypt function
        decrypt(cipher, shift)
    #ask the user if they want to encrypt another text
    another = input("Do you want to encrypt another text? (y/n): ")
    #if the user wants to encrypt another text
    if another == "y":
        #call the encrypt function
        Ciphey()
    #if the user does not want to encrypt another text
    else:
        #exit the program
        exit()


Ciphey()