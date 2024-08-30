# Crie um programa que emprima o menor elemento da lista, utilizando a extrutura for

# Storing data
lista = [1,2,3,4,5,10,39,0]
smaller = lista[0] # Storing the index of the fist element from list
bigger = lista[0]
for e in lista:
    if e < smaller:
        smaller = e
        break
    for e in lista:
        if e > bigger:
            bigger = e
print(f'The smaller element in list:    {smaller}')
print(f'The bigger element in list:     {bigger}')