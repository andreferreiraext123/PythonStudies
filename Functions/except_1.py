# O bloco responsável por tratar as excecoes é o try, ou seja nele que ficara o bloco onde pode vir o erro
    # o bloco try permite delimitar o código onde pode gerar a excecao.
try:
    num = input("Enter a number: ")
    print(num)
except ValueError: # Aqui será tratado o erro, ou seja, dependendo do tipo de erro será apresentada uma mensagem diferente
    print("Enter just numbers!")

# Cada excecao tem um tipo diferente, que nos levar a tratalo, de forma diferente, por exemplo. A excecao Valuerro, mostra que o valor de input é de um tipo diferente que nao é aceito.

# Se nenhum erro ocorrer os códigos dentro de except nao será executado

# Existem vários tipos de excecao no Python, o tipo raiz chama-se Exception, ele cobri maioria das excecoes mais comuns.
    # Isso nos ajudo pois podemos mapear um volume maior de erros, sem precisar colocar diversas clausas de tratamento.
    # Ou seja, podemos mapear um número enorme de excecoes com apenas um tipo raiz.

names = ["André", "Luiz", "Felipe", "Joao"]
for tentativa in range(4): # O bloco abaixo será executado 4 vezes (Contado as tentativas que deram erro)
    try:
        i = int(input("Digite o indice que quer imprimir"))
        print(names[i])
    except ValueError:
        print("Apenas número inteiros!")
    except IndexError:
        print("Apenas dentro do intervalo númerico!")        