tuplas_1 = 'Meu nome é ',
tupla_2 = 'André',

tupla = tuplas_1 + tupla_2
print(tupla) # Output: ('Meu nome é ', 'André')

# Iterando sobre elementos de uma lista dentro de uma tupla
tupla_com_lista = ([1,2,3,4],)
tupla_com_lista[0].append(1)
print(tupla_com_lista)