# Storing data
plate = 0
pilha = list(range(1, plate+1))

while True:
    print(f"\nQuantidade de pratos:   {len(pilha)}")
    print(f"Lista de pratos:    {pilha}")
    print(f"Digite A: Empilhar prato")
    print(f"Digite B: Desempilhar prato")
    print(f"Digite S: Encerrar programa\n")

    operacao = input("Digite a operacao desejada (A|B|S):  ").lower()
    
    if operacao == "b":
        if len(pilha) > 0:
            desempilhar = pilha.pop(-1)
            print(f"Prato N {desempilhar} foi retirado")
        else:
           print("Lista de pratos vazia!")
    
    elif operacao == "a":
        plate += 1
        pilha.append(plate)
        print("Prato empilhado")

    elif operacao == "s":
        print("Programa Encerrado!!!")
        break
    
    else:
        print("Valor inválido!")