# Rewrite the program from program 8.2 using 'for' instead of 'while

def sum(list_):
    total = 0
    for element in list_:
        total += element
    return total
list_ = [10,30,30,2,4,2,9]

print(sum(list_))