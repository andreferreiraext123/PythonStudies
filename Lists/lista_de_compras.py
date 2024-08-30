# Faça um programa que leia itens de uma lista de compras, a cada nova interaçao na lista o programa deve imprimir a lista.

lista_compras = []

while True:
    item = str(input('Enter the item for add in shopping list:  ')).lower()
    if item == 'fim':
        print(f'Shopping list:  {lista_compras}')
        break
    lista_compras.append(item)
    print(f'Shopping list:  {lista_compras}')