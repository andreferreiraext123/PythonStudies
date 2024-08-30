# This method returns True if all characters in the string are not empty and are only letters and/or numbers, without spaces or commas.

# Storing string
string = 'Hey guys how are you?'
string_1 = 'Heyguyshowareyou?'
string_2 = '123'
string_3 = '123 '

operation = string.isalnum()
print(operation) # Output: False

operation = string_1.isalnum()
print(operation)

operation = string_2.isalnum()
print(operation)

operation = string_3.isalnum()
print(operation)

# The method isalph is more restrictive only returns True if all characters are letters
operation = string.isalpha()
print(operation)

# The method isdigit cheeck if all characters are numbers with out spaces
operation = string.isdigit()
print(operation)

operation = string_2.isdigit()
print(operation)