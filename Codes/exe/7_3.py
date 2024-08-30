# Write a program that reads two strings and generates a third one that returns the characters that are only in one of them.

# Storing the strings
strin_0 = input('Insert a random string:    ')
string_1 = input('Insert a random string:   ')

# modifying strings to sets
set_0 = set(strin_0)
set_1 = set(string_1)

# Operation than returns only the characteres that be in only one of them
difference = set_0.symmetric_difference(set_1)

# Now getting the value of the variable 'differnce' and turning it into a string
string_2 = ''.join(difference)

print(string_2)