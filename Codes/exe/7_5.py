# Write a program that reads two strings and generate a third, that be the caracters from string 1 less string 2

# Storing data
string_0 = 'AATTGGAA'
string_1 = 'TG'

list_0 = []
list_1 = []

x = 0

for char in string_0:
    if x >= len(string_1):
        break
    elif char == string_1[x]:
        list_1.append(char)
        pass
    #else:
    #    list_0.append(char)
    x += 1

print(list_0)
print(list_1)