# Tuplas sao como listas mas sendo imultável ou seja, nao pode ter seus valores auterados e utilizndo parenteses(opcionais) no lugar de colchetes.

tuple = ("Ola", "Bom", "Dia")
print(tuple)

tuple = "Ola", "Bom", "Dia"
print(tuple)
#del tuple[0]TypeError: 'tuple' object doesn't support item deletion

# As tuplas nao suportam operaçoes de alteraçoes em seus elementos, adicao o subtracao de quais quer de seus elementos
lista = []
lista.append(1)
print(lista)
del lista[0]
print(lista)