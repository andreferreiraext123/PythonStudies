# O método find serve para procurar o a posicao de uma string dentro de uma string
# Ele conta cada caracter como um indice, da esquerda a direita, considerando o elemento do parametro como sendo um único indice.

# Caso nao seja encontrado o valor procurado irá ser retornado -1

string = 'Olá pessoal, me chamo André.'
find = string.find('André') # Return: 22
find_2 = string.find('Mateus') # Return: -1 
print(find)
print(find_2)

# Caso queria pesquisar da direita, utilize o método (rfind)
find_right = string.rfind('André.')# Output: 0
print(find_right)