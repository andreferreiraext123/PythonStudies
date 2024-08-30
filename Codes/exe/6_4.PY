# O que acontece quando nao verificamos se a lista está vazia e adicionamos o metodo POp?

lista = []

pop = lista.pop(0)

# O metodo pop, excluí o elemento da lista com base no indice, e retorna o seu valor. (Mesmo assim tendo excluído)
# Se nao há elemento para excluir ele nao vai conseguir retornar nada. Entao vai dar erro (Pois nao encontra o elemento) IndexError empty list

