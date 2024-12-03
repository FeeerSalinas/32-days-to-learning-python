#librarys
import random

#array with letters
chars = 'abcdefghijklmnoqprstuvwxyz1234567890!@#$%^&*()_+'
#array to save password
password = ''
#size to password
size = int(input("Write the size of password: "))

for c in range(size):
    #create password
    password += random.choice(chars)
print(password)