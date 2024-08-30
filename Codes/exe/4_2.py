# Faça um programa que pergunte a velocidade de um carro, e aplique uma multa no valor de R$5 por kilometro caso ele ultrapasse 80KM/h.

# Armazenando dados
velocidade_kmh = int(input("Qual é a velocidade do veículo: "))
velocidade_maxima = 80

# Condiçao de verifificacao da aplicabilidade de multa
if velocidade_kmh <= 80:
    print("O veículo está dentro da velocidade permitida: ")
else:
    multa = (velocidade_kmh - velocidade_maxima)*5 # Calculo da multa por Km. (5$ por Km acima da permitida)
    print(f"O veículo está acima da velocidade permitida de {velocidade_kmh} KM/h, o carro foi multado no valor de {multa}R$ ")