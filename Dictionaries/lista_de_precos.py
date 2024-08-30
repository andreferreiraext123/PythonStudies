# Faça um programa que pergunte o preço de um item de uma lista, e retorne o valor desse item.

lista_produto = {
    "Uva": 10.2,
    "Banana": 2.1,
    "Macarrao": 9.0,
    "Virtus": 60.000
}

while True:
    item = str(input("Enter the product's name for tell the price:   "))
    
    if item == 'fim':
        print('\nProgram finished!')
        break
    if item in lista_produto:
        print(f'Price:  {lista_produto[item]}')
    else:
        print('Product not found!')