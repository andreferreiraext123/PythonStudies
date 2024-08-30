lista = [2,3,1,8,9]
x = 0
n = len(lista)

while x < len(lista):
    for i in range(n-1):
        if lista[x] > lista[x+1]:
            lista[x],lista[x+1] = lista[x+1], lista[x]
    x +=1

print(lista)