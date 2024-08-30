# Faça um Aplicativo que calcule o valor a pagar pelo fornecimetno de enegia elétrica
# Pergunte a quantidade de KWh consumida 
# E pergunte o tipo de instalaçao(R = Resistencia, I = para indústrias, C = Comércios)
# Calcule e mostre o valor a pagar

# Entrada de dados
kwh = int((input("Quantos KWh foram consumidos? ")))
    # Tipo de instalacao
print("Resindêncial    :R")
print("Comercial:      :C")
print("Industrial:     :I")
tipo_instalacao = str(input("Qual é o tipo de instalacao elétrica? "))

# Calculo do pagamento
if tipo_instalacao == "R": # Residencial
    tipo_instalacao_1 = "Residencial"
    if kwh < 500:
        preco_kwh = 0.40
    else:
        preco_kwh = 0.65
    valor_conta = preco_kwh * kwh # Valor conta

elif tipo_instalacao == "C": # Comercial
    tipo_instalacao_1 = "Comercial"
    if kwh < 1000:
        preco_kwh = 0.55
    else:
        preco_kwh = 0.60
    valor_conta = preco_kwh * kwh # Valor conta

elif tipo_instalacao == "I": #  Industrial
    tipo_instalacao_1 = "Industrial"
    if kwh < 5000:
        preco_kwh = 0.55
    else:
        preco_kwh = 0.60
    valor_conta = preco_kwh * kwh # Valor conta
else:
    print("Valor insirido inválido! Escolha a categoria correta!")
    preco_kwh = 0
    valor_conta = 0

# Imprimindo resultados
print(f"A quantidade de KWh consumidas é de: {kwh}")
print(f"A sua instalcao é do tipo {tipo_instalacao_1}")
print(f"O valor a pagar é de R${valor_conta:.2f}")