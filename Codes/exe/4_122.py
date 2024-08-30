# Faça um Aplicativo que calcule o valor a pagar pelo fornecimento de energia elétrica
# Pergunte a quantidade de kWh consumida
# E pergunte o tipo de instalação (R = Residencial, I = para Indústrias, C = Comércios)
# Calcule e mostre o valor a pagar

# Entrada de dados
try:
    kwh = int(input("Quantos kWh foram consumidos? "))
    if kwh < 0:
        raise ValueError("A quantidade de kWh deve ser um número positivo.")
except ValueError as e:
    print(f"Entrada inválida: {e}")
    exit()

# Tipo de instalação
print("Residencial    : R")
print("Comercial      : C")
print("Industrial     : I")
tipo_instalacao = input("Qual é o tipo de instalação elétrica? ").strip().upper()

# Cálculo do pagamento
valor_conta = 0

if tipo_instalacao == "R":  # Residencial
    if kwh < 500:
        preco_kwh = 0.40
    else:
        preco_kwh = 0.65
    valor_conta = preco_kwh * kwh

elif tipo_instalacao == "C":  # Comercial
    if kwh < 1000:
        preco_kwh = 0.55
    else:
        preco_kwh = 0.60
    valor_conta = preco_kwh * kwh

elif tipo_instalacao == "I":  # Industrial
    if kwh < 5000:
        preco_kwh = 0.55
    else:
        preco_kwh = 0.60
    valor_conta = preco_kwh * kwh

else:
    print("Valor inserido inválido! Escolha a categoria correta!")
    exit()

# Imprimindo resultados
print(f"A quantidade de kWh consumidas é de: {kwh}")
print(f"A sua instalação é do tipo: {tipo_instalacao}")
print(f"O valor a pagar é de R${valor_conta:.2f}")