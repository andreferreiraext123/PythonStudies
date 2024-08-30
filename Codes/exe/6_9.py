# Faça um programa onde o usuário escreva 2 elementos que deseja encontrar em uma lista

# Storing data
lista = [1,2,3,4,5,6,7,8,9]
x = 0



# Inputs
elemento_0 = int(input('Enter the first element that you want to find:  '))
elemento_1 = int(input('Enter the first element that you want to find:  '))



while x < len(lista):
    if elemento_0 == lista[x]:
        print(f'Elemento {elemento_0} encontrado no indice {x}')
        break
    x += 1
else:
    print(f'Elemento {elemento_0} nao encontrado')

x = 0

while x < len(lista):
    if elemento_1 == lista[x]:
        print(f'Elemento {elemento_1} encontrado no indice {x}')
        break
    x += 1
else:
    print(f'Elemento {elemento_1} nao encontrado')