# Programa que imprime os primeiros 10 números múltiplos de 3

# Inicializa o contador
count = 0

# Inicializa o número atual
current_number = 0

# Loop até encontrar os primeiros 10 múltiplos de 3
while count < 10:
    if current_number % 3 == 0:
        print(current_number)
        count += 1
    current_number += 1
