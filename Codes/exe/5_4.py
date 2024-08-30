# Only print odd numbers

# Data input
end = int(input("Type the last number: "))
begin = 1 

# Loop through the numbers
while begin <= end:  # Begin needs to be less than or equal to end
    if begin % 2 == 1:
        print(begin)
    begin = begin + 1
