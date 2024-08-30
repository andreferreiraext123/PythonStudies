# Faça um programa que leia 7 notas, as armaze em uma lista, e retorne a media
# Pedindo ao user o input de cada nota

# Store data
notas = []
soma = 0
x = 1

# store grade
while x <= 7:
    nota = int(input(f"Digite a nota {x}:   "))
    notas.append(nota)  # Append the note to the list
    soma += nota
    if x == 7:
        print(f'The average of the grades is {soma / x}') # Priting the media
    x += 1

print(f'The sum between the grades is: {soma}') # Priting the sum