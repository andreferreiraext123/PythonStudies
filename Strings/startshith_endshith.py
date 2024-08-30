# Utilizando os métodos startswith and endswith
    # Startswith: Verifica string possuí os caracteres que estao no parametro do método
    # Endswith: Faz a mesma verificacao, mas verifando no final da string

string = 'André Matos Ferreira'

print(string.startswith("André")) # Return: True
print(string.endswith("Matos")) # Return: False
print(string.endswith("Ferreira")) # Return: True


# Utilizando os métodos lower and upper:
    # Ambos os métodos retornam uma cópia dos caracteres da string,em lower = minusculo, upper = maiusculo
print(string.lower()) # Output: 'andré matos ferreira'
print(string.upper()) # Output: 'ANDRÉ MATOS FERREIRA'

print(string.lower().startswith('André')) # Output: False
print(string.upper().startswith('André')) # Output: False
print(string.lower().startswith('andré')) # Output: True
print(string.upper().startswith('ANDRÉ')) # Output: True

# Verificando se uma palavra está presente em uma string
verificando_palavra_in_string = "André" in string
print(verificando_palavra_in_string) # Output: True

string = 'Joao comprou um carro'

print('joao' in string) # Output: False
print('joao'in string.lower()) # Output: True
print('CARRO' in string.upper()) # Output: True

# Usando o not in, serve para verificar se um certo parametro encontrasse em outro, mas trazendo o resultado invertido
print('joao' not in string) # Output: True
print('MACACO' not in string.upper()) # Output: True

# Para fazer a contagém de ocorrencias de letras ou palavras dentro de uma string, pode-se usar o método count.
indios = 'Um indio, dois indio, tres indio'
print(indios.count('indio')) # Output: 3
print(indios.count('o') + indios.count('i')) # Output: 7
print(indios.count('i')) # Output: 7