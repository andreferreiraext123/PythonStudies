# Faça com que o código abaixo aceito multiplos comandos de uma vez só

# Storing data
ultimo_01 = 10
ultimo_02 = 10
fila_01 = list(range(1, ultimo_01 + 1))
fila_02 = list(range(1, ultimo_02 + 1))

# FIFO
while True:
    print("Total de clientes em cada lista")
    print(f"Lista 01: {len(fila_01)}")
    print(f"Lista 02: {len(fila_02)}")
    print(f"Fila 01: {fila_01}")
    print(f"Fila 02: {fila_02}")
    print("\nDigite F: Adicionar clientes na fila 01")
    print("Digite G: Adicionar clientes na fila 02")
    print("Digite A: Realizar atendimento na fila 01")
    print("Digite B: Realizar atendimento na fila 02")
    print("Digite S: Sair")

    operacao = input("\nOperacao ( F | G | A | B | S):    ")
    
    # Operacoes dos clientes nas filas 01 e 02
    if operacao == "A" or operacao == "a":
        if len(fila_01) > 0:
            atendido = fila_01.pop(0) # O metodo pop retorna o elemento eo excluí da lista 01
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia ninguem para atender!") # Condicao se verdadeira print que nao há ninguem para atender
    elif operacao == "B" or operacao == "b":
        if len(fila_02) > 0:
            atendido = fila_02.pop(0) # O metodo pop retorna o elemento eo exclui da lista 02
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia ninguem para atender!")

    # Operacao de adicionar novo cliente a as listas      
    elif operacao == "F" or operacao == "f":
        ultimo_01 += 1 # Incrementa o ticket do novo cliente
        fila_01.append(ultimo_01) # Fila 01

    elif operacao == "G" or operacao == "g":
        ultimo_02 += 1 # incremento do ticket do novo cliente
        fila_02.append(ultimo_02) # Fila 02

    # Operacao de encerramento
    elif operacao == "S" or operacao == "s":
        break
    else:
        print("Operacao inválida! Digite apenas F, G, A, B ou S!")