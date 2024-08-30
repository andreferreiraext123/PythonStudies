# Também é possível se utilizar a funcao len em lista, a funcao len, retorna a quantiade de elementos presentes na lista
# Exemplo 1
lista = [1,2,3,4,5]
print(len(lista)) # Contagem de elementos na lista
print()

# Exemplo 2 - Utilizando a funcao len para imprimir cada elemento da lista
#Stroring data
lista = [1,2,3,4,5,6]
x = 0
while x < len(lista):
    print(lista[x]) # Imprimindo cada elemento da lista pelo indice x
    x += 1 # Acumulando de 1 em 1, representando o indice da lista