lista = ['A', 'B', 'C']
del lista[1]
print(lista)

lista = ['A', 'B', 'C']
del lista[:]
print(lista)



lista = list(range(101))
del lista[1:99]
print(lista)