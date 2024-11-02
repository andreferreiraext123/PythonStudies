import types

def print_lists(list_, nivel=0, caractere=" ", caracteres_por_nivel=2):
    for element in list_:
        if isinstance(element, int):
            # Use o caractere e a contagem de espaços de acordo com o nível
            print(f"{caractere}{element:{' ' * (nivel * caracteres_por_nivel)}}")
        else:
            # Chama a função recursivamente, aumentando o nível
            print_lists(element, nivel + 1, caractere, caracteres_por_nivel)

list_ = [1, [2, 3, 4], [5, 6, [7, 8, 9]], 10]
print_lists(list_)
