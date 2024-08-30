words = ["apple", "banana", "apple", "orange", "banana", "apple", "kiwi", "orange", "kiwi", "kiwi"]

word_count = {}

for word in words:
    # dentro do dicionário, acessando a lista 'words'como keys, ele pega itera sobre cada key na lista, caso a key tenha valor vazio ele retorna 0 como valor dessa key, e incrementa 1 ao valor dessa chave. E itera sobre cada palavra da lista, salvando as iteraçoes no dicionário 'word_count'.
    word_count[word] = word_count.get(word, 0) + 1
    print(word_count)
# Imprimir o dicionário resultante