L = [1, 2, 3, 4, 5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x > (fim - 1):
        if L[x] > L[x + 1]:  # Apenas a condição de verificação foi alterada
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)

# A verificacao ocorrerá normalmente, mas como a lista já está ordenada o resultado será o mesmo.
#lista já estiver ordenada, nenhum elemento é maior que o elemento seguinte.
# Desta forma, após a primeira verificação de todos os elementos,
# o loop interno é interrompido pela condição de (9)