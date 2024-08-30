# Impressao de compras

produto_1 = ['Maça', 10, 0.3]
produto_2 = ['Pera', 5, 0.75]
produto_3 = ['Kiwi', 4, 0.98]
compras = [produto_1, produto_2, produto_3]

for element in compras:
    print(f'Produto: {element[0]}')
    print(f'Quantidade: {element[1]}')
    print(f'Preço:  {element[2]:5.2f}')
    print()