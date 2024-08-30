# Escreva um programa pergunte o valor de um depósito inicial
# Pergunte a taxa de juros de uma poupança
# Exiba os valores mes a mes. Durante os primeiros 24 meses
# Exiba o total ganho com juros no período

# Entrada de dados
deposito_inicial = float(input("Digite o valor do depósito inicial: "))
taxa_juros = float(input("Qual é a taxa de juros mensal (em %)? "))

# Inicializando variáveis
saldo = deposito_inicial
total_juros_ganhos = 0
mes = 1

# Aplicando os juros e exibindo os valores mês a mês
while mes <= 24:
    juros_ganhos = saldo * (taxa_juros / 100)
    saldo += juros_ganhos 
    total_juros_ganhos += juros_ganhos
    print(f"Valor no mês {mes}: R$ {saldo:.2f}")
    mes += 1

# Exibindo o total ganho com juros no período
print(f"Total ganho com juros em 24 meses: R$ {total_juros_ganhos:.2f}")
