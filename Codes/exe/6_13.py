# Faça um programa que emprima o menor, maior eo valor médio em uma lista (Emprimindo os tres valores)
# Menor, Maior, Média
# Example 1
lista = [-10,-8,0,1,2,5,-2,-4]
menor = lista[0]
maior = lista[0]
soma = 0

for element in lista:
    if element < menor:
        menor = element
print(f'Smaller:   {menor}')

for element in lista:
        if element > maior:
            maior = element
print(f'Bigger:   {maior}')

for element in lista:
    soma += element
average = soma / len(lista)
print(f'Average:    {average}')

# Example 2

lista = [-10, -8, 0, 1, 2, 5, -2, -4]
menor = lista[0]
maior = lista[0]
soma = 0

for element in lista:
    if element < menor:
        menor = element
    if element > maior:
        maior = element
    soma += element

average = soma / len(lista)

print(f'Smaller: {menor}')
print(f'Bigger: {maior}')
print(f'Average: {average}')