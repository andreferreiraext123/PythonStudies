# Programa 4.2: carro novo ou velho, dependendo da idade

# Entrada de dados
idade = int(input("Digite aqui quantos anos o veículo tem: "))

# Codiçao: Se o carro tiver menos de 3 anos ele é novo se tiver mais é velho
if idade < 3:
    print("O seu carro é novo!")
if idade > 3:
    print("O seu carro é velho!")
else:
    print("O Seu carro está quase velho!")
