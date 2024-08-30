# Faça um programa que pergunte a quantidade de dias que o cliente utilizou o carro e a kilometragem percorrida. Sabendo que o carro custa 60$ por dia, e o,15R% por km. E apresente o valor a ser pago.

# Atribuindo valores de input

dias_alocado = int(input("Digite aqui a quantidade de dias de utilizacao do veiculo: ")) # Cada dia alocado custam, 60R$
kilometros_rodados = float(input("Digite aqui a kilometragem rodada do veículo: ")) # Cada KM rodado custam, 0,15R%

# Calculo do valor a ser pago pelo cliente
valor = (dias_alocado*60) + (kilometros_rodados*0.15)

# Imprimindo valor a ser pago pelo cliente
print(f"O valor a ser pago ao veículo é de {valor}, foi utilzado por {dias_alocado} dias e {kilometros_rodados} kilometros.")
