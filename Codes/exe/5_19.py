# Contagem de cédulas e moedas

# Armazenando variáveis
valor = float(input("Digite o valor a pagar: "))
cedulas = 0
atual = 10000  # Maior cédula disponível em centavos (R$ 100,00)
apagar = int(valor * 100)  # Convertendo o valor para centavos

# Condição de contagem de cédulas e moedas
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        if cedulas > 0:
            print(f"{cedulas} cédula(s) de R${atual / 100:.2f}")
        if apagar == 0:
            break

        # Transição entre diferentes denominações
        if atual == 10000:
            atual = 5000
        elif atual == 5000:
            atual = 2000
        elif atual == 2000:
            atual = 1000
        elif atual == 1000:
            atual = 500
        elif atual == 500:
            atual = 200
        elif atual == 200:
            atual = 100
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 25
        elif atual == 25:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        elif atual == 1:
          atual == 0.50
        elif atual == 0.50:
            atul = 0.001
        cedulas = 0
