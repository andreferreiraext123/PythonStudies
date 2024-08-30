"""
A operação de união em conjuntos é uma operação matemática que resulta em um novo conjunto contendo todos os elementos únicos presentes em pelo menos um dos conjuntos originais. 
Em outras palavras, a união de dois conjuntos A e B.
É um conjunto que contém todos os elementos de A e todos os elementos de B, sem duplicatas.
"""
# Operacao de uniao Exe 1:
conjunto_A = {1,2,3,4}
conjunto_B = {3,4,5,6}
uniao_0 = conjunto_A | conjunto_B
print(uniao_0)

# Usando o metodo union(). Exe 2:
conjunto_A = {1,2,3,4}
conjunto_B = {3,4,5,6}
uniao_1 = conjunto_A.union(conjunto_B)
print(uniao_1)

# Usando multiplos conjuntos. Exe 3:
conjunto_A = {1,2,3,4}
conjunto_B = {3,4,5,6}
conjunto_C = {2,3,4,5,6,7,8,9,10}
uniao_2 = conjunto_A.union(conjunto_B,conjunto_C) # Union of three sets
uniao_22 = conjunto_A | conjunto_B | conjunto_C # Union of three sets
print(uniao_2,uniao_22)