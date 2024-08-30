# Armazenando variaveis
mes = 1

# Entrada de dados 
deposito_inicial = float(input(f"Digite o valor do depósito do mes {mes}: "))
taxa_juros = float(input("Qual é a taxa de juros mensal (em %)? "))

# Armazenando variaveis
total_juros_ganhos = 0
mes = 2


# Aplicando os juros e exibindo os valores mês a mês
while mes <=24:
    deposito_inicial = float(input(f"Digite o valor do depósito do mes {mes}: "))
    saldo = deposito_inicial
    juros_ganhos = saldo * (taxa_juros / 100)
    saldo += juros_ganhos 
    total_juros_ganhos += juros_ganhos
    print(f"Valor no mês {mes}: R$ {saldo:.2f}")
    mes += 1

# Imprimindo resultados
print(f"Total ganho com juros em 24 meses: R$ {total_juros_ganhos:.2f}")