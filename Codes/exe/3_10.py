# Faça um programa que caucule o aumento de um salario. Deve solicitar o valor do salario e a porcentagem do aumento. Imprimindo o resultado do salario já com o aumento, e a porcentagem do aumento.

# Armazenando valores
salario = float(input("Digite aqui o valor do salario: "))
aumento = int(input("Digite aqui o valor da porcentagem do aumento:"))

# Calculo de aumento do salario
aumento_cal = (salario + (salario*aumento/100))

# Imprimindo resulado do aumento
print(f"O salario {salario:.2f}, recebeu um aumento de {aumento}%.Parabens o seu salario atual é {aumento_cal:.2f}")
