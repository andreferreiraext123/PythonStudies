# Faça um programa que procure um elemento em uma lista de acordo com o valor digitado pelo usuario
# E retorne uma mensagem positiva ou negativa dependendo do retorno

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
indice = 0

# User input
search = int(input('Which number do you want to find?   '))

for element in lista:
    if element == search:
        print(f'The number was found on index {indice}')
        break
    indice += 1
else:
    print('The number was not found')
