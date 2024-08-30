# Write a function that returns the bigger between two numbers

def bigger(num_1,num_2):
    if num_1 > num_2:
        return num_1
    else:
        return num_2
    
print(bigger(10,20))
print(bigger(30,10))