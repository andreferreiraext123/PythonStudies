# Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento.
# Para salarios superiores a 1250, calcule um aumento de 10%.
# Para os inferiores ou iguais, de 15%.

# Entrada de dados
salario = float(input("Digite aqui o valor do salario: "))

# Condição
if salario > 1250:  # Superior a 1250, aplicação de 10% a mais
    aumento = salario * 0.10
else:  # Inferior ou igual a 1250, aplicação de 15% a mais
    aumento = salario * 0.15

# Cálculo do novo salário
novo_salario = salario + aumento

# Exibindo o resultado
print(f"O salário no valor de R${salario:.2f} recebeu um aumento de R${aumento:.2f}, passando para R${novo_salario:.2f}.")