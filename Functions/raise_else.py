# As excecoes, raise, expetion, excepty, também possuem uma extrutura else, ou seja quando  nao ocorre nenhuma excecao dentro do bloco try, podemos a executar algum bloco de código veja abaixo

while True:
    try:
        number = int(input("Enter a number: (0 = exit)"))
        if number == 0:
            break
    except ValueError:
        print("Invalid Value: Please, enter a number!")
    else:
        print("(else)")
    finally:
        print("(finally)")