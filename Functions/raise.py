# Raise é uma excecao que nos ajuda a tratar erros ou regras de negócios
    # Python é usada para lançar uma exceção de forma explícita. Isso é útil quando você deseja sinalizar que ocorreu um erro em uma condição específica do seu código.

def check_age(age):
    if age < 18:
        raise ValueError("You're minor!") # Working
    elif age == 18:
        raise ValueError("You're eighteen years old!") # Don't working
    print("Testing")
    return True


try:
    check_age(15) # The value that will cheeck if is correct or not, needs to be inside the command try
except ValueError as minor:
    print(minor)