A = set() # Transformando a variavel a em um conjunto
A.add(1)
A.add(2)
A.add(3)
A.add(1) # Conjuntos nao suportam elementos repetidos-iguais. SERA IGNORADO

print(A)

print(1 in A) # Verifica se o valor do parametro um existe no conjunto do segundo parametro

# Um set (Conjunto) pode ser criado a partir de listas, tuplas e qualquer outra estrutura de dados que seja enumerável.

lista_set = set([1,2,3])
print(lista_set)

conjunto_set = set({1,2,3,4})
print(conjunto_set)

tupla_set = set((1,2,3))
print(tupla_set)

print(len(conjunto_set)) 