# Faça um programa que pergunte o nome do produto, quantidade e preço, e emprima a lista de produtos
# Inputs: Nome do Produto, Quantidade, Preço
# Output: Lista de cada produto

# Data Storing
shopping_list = []

while True:
    name = str(input('Digite o nome do produto:    '))
    if name == 'Stop' or name == 'stop':
        print('Programa encerrado!')
        break
    quantity = int(input('Digite a quantidade:  '))
    price = float(input('Digite o preço:    '))

    shopping_list.append([name,quantity,price])
    print()
    print(shopping_list)