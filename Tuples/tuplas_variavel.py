# Quando a varizavel nao tem limitadores, e sómente pussui um elemento sem virgulas ele é apenas uma variavel

tupla = 1,
tupla_1 = 1

print(type(tupla)) # Output: tuple
print(tupla + tupla) # Output: 1,1
print(tupla) # Output: (1,)
print(len(tupla))

print(type(tupla_1)) # Output: Int
print(tupla_1 + tupla_1) # Output: 2
print(tupla_1) # Output: 1
print(len(tupla_1)) # TypeError: object of type 'int' has no len(),     É APENAS UMA VARIVEL ARMAZENANDO UM INTEIRO

