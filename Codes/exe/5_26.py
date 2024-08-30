# Data Input
num_1 = int(input("Type the first number: "))
num_2 = int(input("Type the second number: "))

# Initialize variables
resto = num_1

# Calculate the remainder using subtraction
while resto >= num_2:
    resto -= num_2

print("The remainder is:", resto)
