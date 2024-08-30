a = 5 # global variable

def change_num():
    a = 7 # internal variable
    print(f"Number changed {a}") # Changing internal variable 
    print()

change_num() # Calling the function that returns a print with the internal variable
print(a)

# Perceba que a variavel a, nao se altera mesmo usando uma variavel com o mesmo nome na funcao
# Isso se deve porque a variavel a criada na funcao é uma variavel interna, ou seja, seu valor somente existe enquanto a funcao é chamada