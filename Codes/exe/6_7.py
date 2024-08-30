"""
- Aramazene uma pilha de parenteses
- Verifique se os parenteses foram abertos na ordem correta

- Pode ser adicionado parenteses a fila sempre que for encontrado um abre parenteses
- E desempilhado a cada fecha parenteses
"""



expressão = input("Digite a sequência de parênteses a validar:")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")
    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força a mensagem de erro
            break
    x = x + 1

if len(pilha) == 0:
    print("OK")

else:
    print("Erro")