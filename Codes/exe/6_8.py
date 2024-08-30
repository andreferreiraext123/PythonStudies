# Storing data
lista = [1,2,3,4,5]
x = 0

elemento = int(input('Digite o elemento que deseja achar:   '))

while x < len(lista):
    if elemento == lista[x]:
        print(f'Elemento encontrado no indice ({x})')
        break
    x += 1
else:
    print('Elemento nao encontrado')