# Input 5 numbers and ask the user for one number, then print it.
# If the user wants to stop the script, give them an option to break the code.

# Store data
numbers = [0,0,0,0,0]
x = 0

# Storing the numbers for the list
while x < 5:
    numbers[x] = int(input(f"Type the number {x + 1}:  "))
    x += 1

# Checking which num the user wants to see
while True:
    choice = int(input("Which position do you want to print? (Type 0 to stop ): "))
    if choice == 0:
        print("\nProgram closed")
        break
    print(f"You choice the number {numbers[(choice - 1)]}")