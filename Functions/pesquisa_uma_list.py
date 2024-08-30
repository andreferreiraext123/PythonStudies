'''
lista = [1,2,3,4]
# A cada interaçao sobre o iteravel ele acessa dois parametros, o indice e o valor desse indice.
for indice, valor in enumerate(lista):
    print(f'Indice {indice}, Valor {valor}')
'''    

# Programa: Pesquisa em uma lista

def pesquisa(lista, valor):
    #Estrutura de repeticao que itera sobre cada indice(x) e elemento(e) da lista
    for x, e in enumerate(lista):
        if e == valor: # Se o elemento for igual ao valor no caso o parametro
            return f'Indice {x}' # Retorna o indice desse elemento
        return None

lista = [1,2,3,54,3243,6,4234,3,6]
print(pesquisa(lista,10))

# Programa: Faça um programa que retorne a média dos valores de uma lista
def average(lista):
    total = 0
    for element in lista:
        total += element
    return total / len(lista)

lista = [10,20,30,10,10]
print(average(lista))

# Funcao de soma
def sum(lista):
    total = 0
    for element in lista:
        total += element
    return total

# Funcao de média
def average_(lista):
    return sum(lista) / len(lista)

print(average_(lista))