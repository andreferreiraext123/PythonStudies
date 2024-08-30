# Crie um programa que calcule o imposto a pagar no imposto de renda: Salarios menos que (1000), o imspoto a pagar é de (0%). 
# para salarios entre (1000 e 3000), pagariamos (20%) de imspoto sobre o salario. (Acima de 3000) desses valores a alicota é de (35%) sobre o salrio. Mostrar o valor do imposto.

# Entrada de dados
salario = float(input("Digite aqui o salrio para o calculo do imposto de renda: "))
base = salario
imposto = 0

# Condiçao do imposto
if salario > 3000: # 35% imposto acima de 3000
    imposto = imposto + (base - 3000) * 0.35
    base = 3000
if base > 1000:
    imposto = imposto + (base - 1000) * 0.20
