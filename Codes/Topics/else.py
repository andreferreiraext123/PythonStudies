# Programa categoria x preço 

# Entrada de dados
categoria = int(input("Digite a categoria do produto: "))

# Condiçao
if categoria == 1:
    preco = 10
else:
    if categoria == 2:
        preco = 18
    else:
        if categoria == 3:
            preco = 23
        else:
            if categoria == 4:
                preco = 26
            else: 
                if categoria == 5:
                    preco = 31
                else:
                    print("Número invalido! Digite um número de 1 a 5!") # Caso nenhum dos números forem válidos
                    preco = 0 # É nescessário atualizar o valor, pois caso o bloco seja verdadeiro a variavel terá um valor válido

# Imprimindo resultados 
print(f"O preço do produo é {preco:.2f}") # Valor somente será imprimido caso o bloco onde a variavel se encontre for válida. Caso contrário ele nao terá como imprimir o valor da várivel.