# Programa 4.9: Categoria x preço usando elif

# Entrada de dados
try:
    categoria = int(input("Digite aqui o número da categoria: "))
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")
    categoria = None
    
# Condiçao - Categorias
if categoria == 1:
    preco = 10
elif categoria == 2:
    preco = 15
elif categoria == 3:
    preco = 20
elif categoria == 4:
    preco = 25
elif categoria == 5:
    preco = 30
else:
    print("A categoria nao foi encontrada! Digite um número de 1 a 5!")
    preco = 0

# Imprimindo resultados
print(f"O número escolhido foi {categoria}, o valor é de R${preco}")