# Escreva um programa que calcule o tempo de um percurso. Pergunte  a distancia e a velocidade média esperada para a viagem.

# Armazenando os valores dos Inputs
distancia_km = float(input("Digite aqui a distancia em Kilometros do percurso: "))
velocidade_kh = float(input("Digite aqui a velocida média percorrida em KM por hora: "))

# Conculo do tempo estimado do percurso
tempo_percuso = distancia_km / velocidade_kh

# Imprimindo o tempo estimado do percurso
print(f"O tempo estimado para o percurso é de {tempo_percuso} horas")