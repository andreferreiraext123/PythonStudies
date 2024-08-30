# Acessando caracteres de uma string

string = "André Lindo"
print(string[0]) # Possível imprimir e acessar os caracteres de uma sring.

# modificando = string[0] = 'O' # Nao é possível modificar os caracteres de uma string
# print(modificando) 

lista_string = list(string)
for element in range(len(lista_string)):
    lista_string[element] = 'i'

print(lista_string)