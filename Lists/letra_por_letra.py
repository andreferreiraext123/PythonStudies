# Acessando letra por letra de uma string em uma lista

# Exempla 1: Utilizando duas vezes o indice, o primeiro para localizar o elemento da lista eo outro para localizar a posicao do caracter do elemento.

clothes_list = ['Skirt', 'Thoursers', 'Pants', 'Dress', 'Shirt', 'Jacket', 'Shoes']

print(clothes_list[0][0])
print(clothes_list[0][1])
print(clothes_list[0][2])
print(clothes_list[2][2])

# Exempla 2: Utilizando a estrutura de repeticao for, para acessar cada elemento da lista, e depois cada elemento do elemento.

clothes_list = ['Skirt', 'Thoursers', 'Pants', 'Dress', 'Shirt', 'Jacket', 'Shoes']

for element in clothes_list:
    for character in element:
        print(character)