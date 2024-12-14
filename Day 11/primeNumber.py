def primeNumberChecker(num):
    # num<2 isn't prime
    if num < 2:
        return False
    
    # check 2 to sqrt
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    # if no exit divisors it's prime
    return True

num = int(input("Enter a number: "))

if primeNumberChecker(num):
    print("It's prime")
else:
    print("It's not prime")