# Desempacotamento: É quando você pega os valores de uma variável que contém múltiplos itens e os atribui a variáveis separadas.

import time
a,b,c,d,e = 10, 20, 30, 40, 50

print(a)
print(b)
print(c)
print(d)
print(e)

time.sleep(2)
a = 99
b = 99

tuple = a,b

print(a)
print(b)