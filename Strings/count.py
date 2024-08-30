# Para fazer a contagem de ocorrência de letras ou palavras em uma string utilize o método count

phrase = "Era uma vez um leao que adora comer carne de boi. E se chamava Pumba"
tries = 5
answer = phrase.count('a')
underline = "-"*50

while tries > 0:
    print(f'Número de tentativas! {tries}')
    choice = int(input('Quantos vezes a letra (a) aparece no texto?  '))
    if choice == answer:
        print(f'{underline}\nParabéns voce acertou!\nO números de ocorrências da letra (a) é de {answer}\n{underline}')
        break
    elif choice != answer:
        print('Voce errou! Tente novamente!')
    tries -= 1