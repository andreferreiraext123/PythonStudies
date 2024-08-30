# Verificando se um conjunto contém o outro
A = {1,2,3,4,5}
B = {1,2,3,4}

# Verifica se todos os elementos de B estão em A
print(A > B) # True, porque todos os elementos de B estão em A

# Verifica se todos os elementos de A estão em B
print(B > A) # False, porque nem todos os elementos de A estão em B

# Verifica se A contém A
print(A > A) # False, um conjunto não pode ser propriamente maior que ele mesmo

# Verificando se um conjunto é maior ou igual a outro (contém outro)
print(A >= B) # True, porque A contém todos os elementos de B

# Criando um conjunto de números pares de 0 a 8 usando compreensão de conjuntos
pares = {numero for numero in range(0, 10, 2)}
print(pares) # {0, 2, 4, 6, 8}

# Verificando se um conjunto possuí elementos igual ao outro
print(A == B) # False, porque A nao possuí os mesmo elementos que B

# Verificando se um conjunto possuí elementos diferentes do outro
print(A != B)# True, porque um dos conjuntos possuí um elemento que nao está presente no outro

# Aplicando uma operacao de verificacao que retorna um booleano a partir de uma variavel que possuí um conjunto e um conjunto criado como paremetro na operacao
print(B != {1,2,3,4}) # False, pois os elementos do conjunto B sao os mesmos do conjunto apresentado na operacao
print(B == {1,2,3,4}) # True, porque os elementos presentes no conjunto B sao os mesmos presentes no conjunto da operacao

# Os conjutos nao possuí uma ordem pré-estabelicidade de seus elementos e nao permite o acesso por index de seus elementos
print(B[0]) # TypeError: 'set' object is not subscriptable