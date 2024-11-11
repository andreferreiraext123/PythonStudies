def generator():
    i = 0 # E nao daqui
    while True:
        yield i # Toda vez que a funcao for chamada ela comecara daqui
        i += 2

g = generator()

print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# O programa cria uma sequencia de numeros infinita. Vamos testa-lo com um 'for' que chama a funcao

for item in generator():
    print(item)