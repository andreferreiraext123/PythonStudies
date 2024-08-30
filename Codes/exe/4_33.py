# Escreva um programa que leia três números e que imprima o maior e o menor

# Entrada de dados
number_1 = int(input("Digite aqui o 1. número: "))
number_2 = int(input("Digite aqui o 2. número: "))
number_3 = int(input("Digite aqui o 3. número: "))

# Inicializando maior e menor com o primeiro número
maior = number_1
menor = number_1

# Verificando o maior número
if number_2 > maior:
    maior = number_2
if number_3 > maior:
    maior = number_3

# Verificando o menor número
if number_2 < menor:
    menor = number_2
if number_3 < menor:
    menor = number_3

# Exibindo o resultado
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")