# Solicitar ao usuário que digite um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é primo
if numero > 1:  # Números menores ou iguais a 1 não são primos
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"{numero} não é primo.")
            break # Interrompendo o ciclo
    else:
        print(f"{numero} é primo.")
else:
    print("Números menores ou iguais a 1 não são considerados primos.")
