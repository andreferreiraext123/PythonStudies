# Using functions as parameters
# We need to use three functions, one that is the functions main, will print the list
    # More two that be the parameters, one for check if the element is odd, and other for check if is even.
        # And more one for print the elements tha the conditions was true


def print_list(lista, print_element,condition):
    for element in lista:
        if condition(element):
            print_element(element)

# This function will return just even elements
def even(element):
    return element % 2 == 0

# This function will return just odd elements
def odd(element):
    return not even(element)

# This function will print the elements
def print_element(element):
    print(f"Value {element}")


lista = [1, 7, 9, 2, 11, 0]

test_0 = print_list(lista, print_element, even) #Outputs: Value 2, Value 0
test_1 = print_list(lista, print_element, odd) #Outputs: Value 1, Value 7, Value 9, Value 11