# Escreva um programa que irá calcular o valor da corrida de acordo com a distancia em KMs, que será percorrida
# Pergunte qual é a distancia em KMS que o passageiro deseja percorrer
# Calcule o preço, cobrando R$ 0.50 por KM se a distancia for de até 200kM
# Calcule o preço, cobrando R$ 0.45 por KM se a distancia for maior que 200KM

# Entrada de dados
distancia = float(input("Qual é a distancia em KMs até o seu trajeto? "))
passagem = 0

# Verificando valor da passagem
if distancia > 200:
    preco_por_km = 0.45
else:
    preco_por_km = 0.50

passagem = distancia * preco_por_km

# Exibindo resultados 
print(f"O valor da passagem é de R${passagem:.2f}, para uma distância de {distancia}KM.")