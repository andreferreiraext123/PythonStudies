# Write a program that reads a string and prints how many times each character will be in the string.

string = 'TTAAC'
chars = ['T', 'A', 'C']

#counting = string.count(chars[0])

for char in chars:
    print(string.count(char))