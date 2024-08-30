# Storing the string
string = "  Once upon a time there was a pudding in love  "

# Attempting to remove all the spaces from the string (Note: strip methods only remove leading/trailing spaces)
strip_op = string.strip()   # No change as there are no leading or trailing spaces

# Removing spaces from the right of the string
rstrip_op = string.rstrip()  # No change as there are no trailing spaces

# Removing spaces from the left of the string
lstrip_op = string.lstrip()  # No change as there are no leading spaces

# Printing the operations
print(f"Strip: {strip_op}")
print(f"RStrip: {rstrip_op}")
print(f"LStrip: {lstrip_op}")