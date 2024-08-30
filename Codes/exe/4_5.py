# Faça um programa que diga se o carro é velho ou novo
# Deve dizer que o carro é velho se a idade for maior que 3
# E dizer que o carro é novo se for menor que 3

# Entrada de dados
idade = int(input("Quantos anos tem o seu carro? "))

# Condiçao, verificando se o carro é velho ou novo
if idade <= 3:
    print("O seu carro é novo")
else:
    print("O seu carro é velho")