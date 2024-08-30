# Faça um programa que calcule a quantidade de tempo perdida de vida de um fumante. Com base na quantidade de cigarros por dia, e quanto anos ele fuma. Considerando que um fumante perde 10min de vida a cada cigarro. E exiba o tempo perdido em dias.

# Entrada de dados

cigarro_diario_qnt = int(input("Digite aqui a quantidade de cigarros por dia: "))
anos_fumando = int(input("Digite aqui a quantidade de anos, sendo fumante: "))

# Calculo de perda de tempo de vida, com base na quantidade de cigarros diarios e os anos como fumante.
tempo_perdido = (anos_fumando * 365 * cigarro_diario_qnt * 10) / 1440   # Sabendo que a cada cigarro perde-se 10min de vida.

# Imprimindo resultado
print(f"Com base na quantidade de cigarros consumidos diariamente igual a {cigarro_diario_qnt} cigarros diarios. E {anos_fumando} anos como fumante. Voce tem menos de {tempo_perdido:.0f} dias de vida.")