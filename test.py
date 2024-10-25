# Do a program that try to identify a random number, the user will have three tries
    # Conditions: If the user right the program finish, and if the user wost the three tries the program also end.

import random

tries = 3
# Storing the random number(On the buffer)
num = random.randint(1,10) # between 1 to 10 

while tries >= 1:
    try:
        try_ = int(input("Enter a number: "))
        if try_ == num:
            print("You're right!")
            break
        elif try_ != num:
            print("You're wrong!")
            tries -= 1
            print(f"Tries quantity {tries}")
    except ValueError:
        print("Enter a int number!")
