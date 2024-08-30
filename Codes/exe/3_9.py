# Faça um programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Calcule o total em segundos.

# Armazenando os valores
dia = int(input("Digite aqui os dias: ")) # Quantidade de dias
hora = int(input("Digite aqui os horas: ")) # Quantidade de horas
minuto = int(input("Digite aqui os minutos: ")) # Quantidade de minutos
segundo = int(input("Digite aqui os segundos: ")) # Quantidade de segundos

# Conversao de todos os inputs para segundos
segundos_convertido = (dia*86400) + (hora*3600) + (minuto*60) + segundo

# Imprimindo o acumulo de inputs em segundos
print(f"A quantidade total em segundo é {segundos_convertido}") 