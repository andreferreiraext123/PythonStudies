# Crie um programa que selecione e copie os elementos de uma lista em outras listas

# A lista mae se chama-ra (Valores), e se os elementos da lista Valores forem pares deverao ser copiados na (lista Pares), caso os elementos da lista Valores forem impares deverao ser copiados na (lista impares).

# Data Storing
valores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] 
pares = []
impares = []

for element in valores:
    if element % 2 == 0:
        pares.append(element)

    else:
        impares.append(element)

print(pares)
print(impares)