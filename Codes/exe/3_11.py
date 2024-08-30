# Faça um programa que solicite o preco de uma mercadoria e o percentual de desconto. Exiba o valor do desconto eo preco a pagar.

# Iniciando os Inputs
preco_produto = float(input("Digite aqui o valor do produto: "))
desconto = int(input("Digite aqui a porcentagem de desconto do produto: "))

# Calculo de desconto do produto
desconto_efetuado = preco_produto - (preco_produto*desconto/100)

# Imprimindo o desconto efetuado no valor do produto
print(f"Valor original do produto {preco_produto:.2f}R$, desconto aplicado {desconto}%, valor do produto com o desconto aplicado {desconto_efetuado:.2f}R$")