# Programa 6.7: Simulacao de uma fila de banco

# Storing data
ultimo = 10
fila = list(range(1, ultimo + 1))

# FIFO
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print(f"Digite F para adicionar um cliente ao final da fila,")
    print("Ou A para realizar o atendimento. S para sair")

    operacao = input("Operacao ( F, A ou S):    ")
    
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0) # O metodo pop retorna o elemento eo excluí da lista
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia ninguem para atender!") # Condicao se verdadeira print que nao há ninguem para atender
    elif operacao == "F":
        ultimo +1 # Incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operacao inválida! Digite apenas F, A ou S!")