# write a program that generates dictionaries
# Each key be a character and your value be a number

dictionary = {}

while True:
    key = input('Enter a key: ')
    if key == 'End':
        break
    
    # Adiciona cada caractere da chave ao dicionário
    for char in key:
        if char not in dictionary:
            # Associa um valor ao caractere (por exemplo, o código ASCII do caractere)
            dictionary[char] = ord(char)
    
    # Iterando sobre cada caractere na chave inserida
    for char in key:
        print(f"Value for {char}: {dictionary[char]}")
    