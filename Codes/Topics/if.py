# Programa que lê dois valores e impre qual é o maior

# Entrada de dados
numero_1 = int(input("Digite aqui o primeiro número: "))
numero_2 = int(input("Digite aqui o segundo número: "))

# Condiçao de verificacao do maior número
if numero_1 > numero_2:
    print("O primeiro número é o maior!")
if numero_2 > numero_1:
    print("O segundo número é maior!")
else:
    print('Números iguais')