"""Adicionando elementos a lista. O metodo append, adiciona elementos ao final da lista.
Em python chamos um metodo escrevendo-o apos o nome do objeto (uma lista é um objeto), é um costume dizer que um metodo é uma funcao de um objeto
"""

lista = []
lista.append("Andre")
lista.append("Matos")
lista.append("Ferreira")

print(lista)

while True:
    num_1 = int(input("Type a num:  "))
    if num_1 == 0:
        break
    lista.append(num_1)
    print(lista)