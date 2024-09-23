# Exeption, é o tipo de excecao raiz do python, onde cobri a maioria dos erros mais comuns em python.
    # Sendo ótimo para mapear uma vasta gama de erros de uma vez

colors = ["Red", "Blue", "Green", "Yellow"]

print("You've four tries!")
for choices in range(4):
    try:
        i = int(input("Enter a number for show a color: "))
        print(f"the chosen color was {colors[(i - 1)]}")
    except Exception as Error: # Tipo raiz, que cobri a maioria dos erros comuns em python
        print("Please, enter with a valid value!")
        print(f"Type error: {Error}") # Imprimindo mensagem de erro, ao tipo de erro especifico
