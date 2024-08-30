# Programa 5.1 Reformulado: Contagem de cédulas

# Armazenamento de dados
valor = int(input("Digite o valor:  "))
cedulas = 0
atual = 50
apagar = valor

# Condiçao de contagem de cédulas
while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cedulas (s) de R${atual}")
        if apagar == 0:
            break
        if atual == 50:
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
