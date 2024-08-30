# E que pergunte qual operacao o usuário deseja realizar.
    # Dando as opçoes de (+,-,/ e *)
# Escreva um programa que leia 2 números
# E exiba o resultado da operacao solicitada

# Entrada de dados
    #Escolha da operacao
print("Adicao:          1")
print("Subtracao:       2")
print("Multiplicacao:   3")
print("Divisao:         4")
operador = int(input("Escolha uma das opçoes: "))

# Entrada de dados
    #Operandos
number_1 = int(input("Escolha um número para o calculo:   "))
number_2 = int(input("Escolha um número para o calculo:   "))

# Condiçao do calculo
if operador == 1: # Adicao
    calculo = number_1 + number_2
    operacao = "+"
elif operador == 2: # Subtracao
    calculo = number_1 - number_2
    operacao = "-"
elif operador == 3: # Multiplicacao
    calculo = number_1 * number_2
    operacao = "*"
elif operador == 4: # Divisao
    calculo = number_1 * number_2
    operacao = "/"
else:
    print("O número digitado é inválido. Digite um número de 1 a 4.")
    calculo = 0

# Exibindo resultados
print(f"O resultado de {number_1} {operacao} {number_2}, é igual a {calculo}.")