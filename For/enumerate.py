# Example 01
lista = [5,9,13]
x = 0
for element in lista:
    print(f'{element}: ({x})')
    x += 1

# Example 02
lista = [5,9,13]
for indice, elemento in enumerate(lista):
    print(f'[{indice}]: {elemento}')