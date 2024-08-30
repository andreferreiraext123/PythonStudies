# Contagem de celulas

# Armazenando variaveis
valor = int(input("Digite o valor a pagar:  "))
cedulas = 0
atual = 100 # Maior cédula disponível
apagar = valor

# Condiçao de contagem de cédulas
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if cedulas > 0:
            print(f"{cedulas} cédula(s) de R${atual}")
        if apagar == 0:
            break

        # Transition between different denominations
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        cedulas = 0

