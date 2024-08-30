# The 'center' method is used to center a string or any other value, between some parameters, such as the number of spaces or other characters that will be centered, the delimiters and what the characters are.


string = 'André'

center = string.center(10)
print(center)

center = string.center(10, '_')
print(center)

center = string.center(10, '_') + ']'
print(center)

center = '[' + string.center(11, '_') + ']'
print(center)