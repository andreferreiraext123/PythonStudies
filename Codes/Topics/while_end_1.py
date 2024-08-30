# Write a script that prints the numbers between 0 and the number inputted by the user.

# Data input
end = int(input("Type the last number to be printed: "))
begin = 0

# Numbers between
while begin <= end:
    if begin % 2 == 0:
        print(begin)
    begin = begin + 1
