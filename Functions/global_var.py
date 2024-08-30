# Global variable, we know that when we initialize a variable inside a function we are creating an internal variable, but if we want to use a global variable, we just need to place the global instructions before initializing the variable.

num = 5

def change_num():
    global num # Calling the global variable
    num = 7 # The value are the same between all variables with the same indentification/name
    print(f"Varible changed:  {num}")

change_num() # Output: 7
print(num) # Output: 7