# Verificando a aprovacao do Aluno

# Atribuindo as notas nas variaveis materias
materia_1 = 6
materia_2 = 8
meteria_3 = 1

# Calculado a média do aluno com base na nota das tres materias
media = ((materia_1 + materia_2 + meteria_3)/3)

# Condicao de aprovacao, média mínima 7.
if media >= 7:
    print(f"Aluno com média {media}, aprovado")
else:
    print(f"Aluno com média {media}, reprovado!")