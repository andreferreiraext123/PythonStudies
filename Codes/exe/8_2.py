# Write a function that inputs two numbers and returns True if the first number is a multiple of the second

def multiple(num_1,num_2):
    if num_1 % num_2 == 0:
        return 'True'
    else:
        return 'False'

print(multiple(8,4))
print(multiple(7,3))
print(multiple(5,5))