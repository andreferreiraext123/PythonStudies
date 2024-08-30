# Criar uma funcao pra encontrar elementos na lista. Retornando o seu indice e parando achado o elemento. E parando o looping assim que achado

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Entradas do usuário
elemento_0 = int(input('Digite o primeiro elemento que você deseja encontrar: '))
elemento_1 = int(input('Digite o segundo elemento que você deseja encontrar: '))

# Encontrar elemento
def EncontrarElemento(lista, elemento):
    for indice, valor in enumerate(lista):
        if valor == elemento:
            print(f'Elemento {elemento} encontrado! No índice {indice}')
            return
        print(f'Elemento {elemento} nao encontrado')

# Buscar pelos elementos
EncontrarElemento(lista, elemento_0)
EncontrarElemento(lista, elemento_1)