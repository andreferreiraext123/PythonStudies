# Faça um programa que some 10 números
# Armazenando variaveis
n = 1   # Contador
soma = 0 # Acumulador

# Acumulando os números
while n <= 10:
    x = int(input(f"Digite o {n} número:    "))
    soma = soma + x
    n = n + 1
print(f"Soma:   {soma}")
