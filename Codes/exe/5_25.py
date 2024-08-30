# Escreva um programa que calcule a raiz quadrada de um número
# Usando o metodo de Newton para obter o resultado aproximado

n = float(input("Digite um número para encontrar a sua raiz quadrada: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.0f}")