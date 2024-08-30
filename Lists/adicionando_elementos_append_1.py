# Create a list where the user can input elements, giving them a stop option for the code. After that, print the number of elements in the list

# Storing data
lista = []

while True:
    element = int(input("Enter an element to add to the list (or 'stop' to finish): "))
    if element == 0:
        break
    lista.append(element)

print(lista) # printing list
print(len(lista)) # quantity of elements from list