# Escreva um programa que leia tres numeros e que imprima o maior e o menor

# Entrada de dados
number_1 = int(input("Digite aqui o 1. numero: "))
number_2 = int(input("Digite aqui o 2. numero: "))
number_3 = int(input("Digite aqui o 3. numero: "))

# Condicao (Verificando Maior número)
if number_1 > number_2 and number_1 > number_3: # Verificando se number_1, é o maior número
    print(number_1)
if number_2 > number_1 and number_2 > number_3: # Verificando se number_2, é o maior número
    print(number_2)
if number_3 > number_1 and number_3 > number_2: # Verificando se number_3, é o maior número
    print(number_3)

# Condicao (Verificando o menor número)
if number_1 < number_2 and number_1 < number_3: # Verificando se number_1, é o menor número
    print(number_1)
if number_2 < number_1 and number_2 < number_3: # Verificando se number_2, é o menor número
    print(number_2)
if number_3 < number_1 and number_3 < number_2: # Verificando se number_3, é o menor número
    print(number_3)