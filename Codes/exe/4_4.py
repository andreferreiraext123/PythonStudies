# Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento. Para salarios superiores a ((1.250), calcule um aumento de (10%)). (Para os inferiores ou iguais, de 15%.)

# Entrada de dados
salario = float(input("Digite aqui o valor do salario: "))
aumento = 0

# Condicao
if salario > 1250: # Superior a 1250, aplicacao de 10% a mais
    aumento = (salario * 0.10)
    print(f"O salario no valor de {salario:.2f}R$, recebeu um aumento no valor de {aumento:.2f}R$")
elif salario <= 1250: # Inferior ou igual a 1250, aplicacao de 15 a mais
    aumento = (salario *0.15)
    print(f"O salario no valor de {salario:.2f}R$, recebeu um aumento no valor de {aumento:.2f}R$")