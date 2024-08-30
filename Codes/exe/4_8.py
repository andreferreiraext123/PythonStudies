# Faça um programa que calcule o valor do plano de uma operadora'
# Primeiro pergunte qual é o plano
    # Depois verifique qual é o preço do plano, e tudo que está incluso para o calculo do valor
# Pergunte os minutos consumidos
    # Depois verifique se os minutos utilizados exederam o limite do plano, e aplique a taxa e retorne o valor a pagar
# Depois retorne todo o custo do cliente

# Entrada de dados
plano = str(input("Qual é o seu plano? "))

# Custos dos planos
if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preco = 50

if plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preco = 99

# Verificando se foi encontrado o plano
if plano != "falopouco" and plano != "falomuito":
    print("Nao encontramos esse plano!")

# Entrada de dados (Minutos consumidos)
minutos_consumidos = int(input("Quanto minutos voce utilizou?"))

# Valor do preco a pagar
if plano == "falopouco" or plano == "falomuito":
    print("Voce vai pagar: ")
    print(f"Preço do plano  R${preco:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento      R${suplemento:10.2f}")
    print(f"Total           R${preco + suplemento:10.2f}")