# Armazenando tabela de preços
tabela = {
    1:  [0.50, "Maça"],
    2:  [1.00, "Pera"],
    3:  [4.00, "Banana"],
    5:  [7.00, "Melancia"],
    9:  [8.00, "Abacaxi"]
}
# Exibindo tabela
print(tabela)

# Armazenando valores
quantiade_produto = 0
valor_total = 0

# input
while True:
    codigo_produto = int(input("Digite o código do produto, ou digite zero para interromper:  "))
    if codigo_produto == 0:
        break
        
    if codigo_produto == 1:
        valor_total += 0.50

    elif codigo_produto == 2:
        valor_total += 1.00

    elif codigo_produto == 3:
        valor_total += 4.00

    elif codigo_produto == 5:
        valor_total += 7.00

    elif codigo_produto == 9:
        valor_total += 8.00

        quantiade_produto += 1

    else:
        print("Código Inválido!")


# Exibindo resultados
print(f"Quantiade de produtos {quantiade_produto}")
print(f"Valor total R$  {valor_total}")