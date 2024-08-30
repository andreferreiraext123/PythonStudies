# Create a program that input two lists and create the third using the twice first

# Example 1
print('Example 1')
#Strong list
firstlist = []
x = 0
while x < 2:
    element = input(f"Creat the list {x+1}:  ")
    firstlist.append(element)
    x += 1
print(firstlist)

# Example 2
print('\n Example 2')

list_01 = ['Andre']
list_02 = ['Matos']
list_03 = []
list_03.append(list_01 + list_02)

print(list_03)

# Example 3 
print('\n Example 3')

lista = []
lista.append(['Vo nada'])
lista.append(['Vou nada'])
lista.append(['Vo nada'])
print(lista)