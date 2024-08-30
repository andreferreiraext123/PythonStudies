lista_0 = [1,2,3,4]
lista_1 = [3,1,2,5,6,7]

# Juntando as listas sem repetir os elementos (Sem manter a ordem)
union_operation = set(lista_0).union(set(lista_1))
print(union_operation) # Output: {1, 2, 3, 4, 5, 6, 7}

# Elementos da lista 0 que nao estao na lista 1. 
diference_operation = set(lista_0) - set(lista_1) # Somente elementos que estao no primeiro conjunto e que nao estao no segundo
print(diference_operation) # Output: {4}

# Elementos únicos, ou seja, que nao se repetem em nenhum dos conjuntos
intersection_operation = set(lista_0) ^ set(lista_1)
print(intersection_operation) # Output: {4,5,6,7}

# Elementos repetidos, ou seja, que estao presentes em ambos os conjuntos
similar_operation = set(lista_0) & set(lista_1)
print(similar_operation) # Output: {1,2,3}