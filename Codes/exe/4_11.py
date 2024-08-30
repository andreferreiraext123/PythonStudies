# Escreva um programa para aprovar um empréstimo bancário para compra de uma casa
# O programa deve perguntar o valor da casa
# O salário do solicitante
# E a quantidade de anos a pagar
# O valor da prestação não deve ser superior a 30% do valor do salário do solicitante
# Caso seja aprovado, continue com o programa, caso não, imprima uma mensagem dizendo que foi recusado
# Calcule o valor da prestação da casa dividido pelo número de meses a pagar, e imprima o resultado

# Entrada de dados
valor_imovel = float(input("Qual é o valor do imóvel? "))
salario = float(input("Qual é o seu salário? "))
anos_de_prestacoes = int(input("Quantos anos prefere dividir as prestações? "))

# Cálculo das prestações
preco_prestacoes = valor_imovel / (anos_de_prestacoes * 12)

# Verificação da aprovação do empréstimo
if preco_prestacoes > (salario * 0.30):
    print("O seu empréstimo foi recusado!")
else:
    print("Parabéns, financiamento aprovado!")
    print(f"O valor do imóvel é de R$ {valor_imovel:.2f}")
    print(f"O preço das prestações divididas em {anos_de_prestacoes} anos, é de R${preco_prestacoes:.2f} por mês")