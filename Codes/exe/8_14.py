import random
random_number = random.randint(1,10) # Storing the random number

# The user only have 3 tries,if he gets correct the program finishes

tries = 3 # Three tries
while tries >= 1:
    choice = int(input("Enter a number, between (from 1 to 10): "))
    if choice == random_number:
        print(f"You choiced the correct number! {random_number}")
        break
    
    elif choice != random_number:
        tries -= 1
        if tries != 0:
            print(f"Try again! You've {tries} tries")
        else:
            print("You lost!")    