def print_bigger(message, *numbers):
    bigger = None

    for element in numbers:
        if bigger is None or bigger < element:
            bigger = element
        # If the value from the variable 'bigger' is equal than None: True
        # Or the variable 'bigger' is less than element: True
        
    print(f"{message}: {bigger}")

list_about_numbers = [1,2,342,4]
print_bigger("Bigger", *list_about_numbers)

# Or in the second way
print_bigger("Max", *[1,2,342,4])