# Programa 4.4: Calculo da mensalidade de um plano de culular da Operadora 'Tchau'

# Entrada de dados
plano = str(input("Qual é o seu plano? "))

# Verificao de planos
if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preco = 50

if plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preco = 100

# Vericando se o nome do plano foi digitado corretamente
if plano != "falopouco" and plano != "falomuito":
    print("Nao conheço esse plano!")

# Condiçao do valor a pagar 
if plano == "falopouco" or plano == "falomuito":
    minutos_consumidos = int(input("Quantos minutos voce consumiu? "))
    print("Voce vai pagar: ")
    print(f"Preço do plano  R${preco:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f"Suplemento      R${suplemento:10.2f}")
    print(f"Total           R${preco + suplemento:10.2f}")