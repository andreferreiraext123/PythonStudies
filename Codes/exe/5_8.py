# Entrada de dados
number_1 = int(input("Type the first number: "))
number_2 = int(input("Type the second number: "))

# Cálculo da multiplicação
calculation = 0  # Inicializa o resultado da multiplicação

# Loop para somar number_1 'number_2' vezes
multiplier = 0
while multiplier < number_2:
    calculation += number_1  # Soma number_1 ao resultado a cada iteração
    multiplier += 1  # Incrementa o contador do loop

# Output
print(f"The result of {number_1} multiplied by {number_2} is: {calculation}")
