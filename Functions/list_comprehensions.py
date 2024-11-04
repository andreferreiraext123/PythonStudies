# Crie uma lista com 'list comprehensions'


list_0 = [item for item in range(10)]

print(list_0)

# Equivalente com a list comprehensions usando estrutura for
list_1 = []
for item in range(10):
    list_1.append(item)


# Criando lista com list comprehensions dentro de uma lista

list_2 = [item * 2 for item in [0,1,2,3]]
print(list_2)

# Fazendo o mesmo do programa anterior utilizando a estrutura for
x = [0,1,2,3]
list_3 = []

for item in x:
    list_3.append(item * 2)
print(list_3)    


# Faca uma lista onde cada elemento e uma tupla, utilizando list comprehensions
list_4 = [(item, item * 2 ) for item in [1,2,3]]
"""
Leitura do programa acima:
    Tranforme faca list_4 uma lista, onde cada elemento chamado item de [0,1,2,3] seja transformado 
    em uma tupla, onde o primeiro elemento da tupla e o proprio item, e o segundo e o dobro de item
    Faca isso para cada elemento da lista
"""
print(list_4)


# Fazendo o mesmo codigo acima utilizando estrutura for
"""
- Ler elementos de uma lista
- Retornar uma lista, onde cada elemento seja uma tupla
- Cada tupla deve conter seu primeiro elemento, sendo o proprio elemento da lista lido,
e o segundo o dobro desse elemento
"""
list_5 = []
for item in [1,2,3]:
    list_5.append((item, item * 2))

print(list_5)    

# list comprehensions tambem pode ser usado para outros tipos de dados
list_6 = [item.upper() for item in ['Andre']]

print(list_6)

# Fazendo o mesmo do que o codigo acima, utilizando a estrutura for

list_7 = []
for item in ['Andre']:
    list_7.append(item.upper())

# O recurso list comprehensions, tambem aceita estrutura de decisao
list_8 = [item for item in range(10) if item % 2 == 0]
print(list_8)

# Dois elementos
list_9 = [(item_0,item_1) for item_1,item_0 in [(4,3), (1,2), (8,9)]]
print(list_9)