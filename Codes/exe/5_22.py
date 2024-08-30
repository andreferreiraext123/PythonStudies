# Iniciando lista de opções
while True:
    print("""
    Menu
    ----
    1 - Adição
    2 - Subtração
    3 - Divisão
    4 - Multiplicação
    5 - Sair
    """)

    # Data input
    opcao = int(input("Escolha uma opção: "))
    if opcao == 5:
        print("Programa encerrado!")
        break
    elif opcao >= 1 and opcao < 5:
        num = int(input("Escolha um número para a tabuada:  "))
        x = 1
    while x <= 10:
        if opcao == 1:
            print(f"{num} + {x} = {num + x}")
        elif opcao == 2:
            print(f"{num} - {x} = {num - x}")
        elif opcao == 3:
            print(f"{num} / {x} = {num / x}")
        elif opcao == 4:
            print(f"{num} * {x} = {num * x}")
        x += 1
    else:
        print("Opçao inválida!")