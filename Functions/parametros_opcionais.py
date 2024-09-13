# No python é possível instanciar uma funcao, possuindo parametros opcnais.
    # Ou seja, caso o usuario nao instancie valores a essa funcao, a funcao executará os valores salvos nela


def multiplicaton_table(table = 2):
    num = 0
    while num <= 10:
        print(f"{table} * {num}" )
        num += 1

print(multiplicaton_table(10)) # Com parametro
print(multiplicaton_table()) # Sem parametro
