# Programa 4.3: Cálculo do impostode reda

#Entrada de dados
salario = float(input("Digite o salario para calculo do imposto: "))
base = salario
imposto = 0

# Aplicando imposto sobre o salario
if salario > 3000:
    imposto = imposto + ((base - 3000)*0.35)
    base = 3000 # Atualizando o valor da variavel (base)
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Salario: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}")

#Deve-se se atentar na volatilidade de dados a uma variavel, uma variavel possuí dados que podem ser alterados ao decorrer do código.

