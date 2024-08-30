# Do a function the returns if a number is even or odd


def épar(num):
    if num % 2 == 0:
        return 'Even'

print(épar(15))

# Reusing the first function in the second function for returns if a parameter is odd of even
def odd_or_even(num):
    if épar(num):
        return 'Even'
    else:
        return 'Odd'
        
print(odd_or_even(10))
print(odd_or_even(15))
