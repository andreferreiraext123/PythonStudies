# Calcule a média de um aluno com base nas notas atribuidas a uma lista

grades = [6, 7, 4, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += grades[x]
    x += 1 
print(f"A média do aluno é: {soma / x:5.2f}")
print(x)