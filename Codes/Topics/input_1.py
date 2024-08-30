# Atribuindo os valores as variaveis
anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bonus = anos * valor_por_ano

# Imprimindo as informaçoes
print(f"Voce tem {anos} anos de serviço, e guardou {valor_por_ano:5.2f} R$ por ano. Tendo um bonus de R${bonus:5.2f}")
