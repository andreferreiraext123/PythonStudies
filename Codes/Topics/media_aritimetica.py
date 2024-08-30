# Calcule a média aritimética
# Entre 5 números
# Utilizando a condiçao While

# Armazenando variaveis
n = 1 # Contador
soma = 0

# Soma dos valores
while n <= 5:
    x = int(input(f"Digite o valor {n}: "))
    soma = soma + x
    n = n + 1

# Calculando média
media = soma / 5

# imprimindo resultados
print(f"A média é {media}")