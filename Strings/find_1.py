# Pesquisando as posiçoes das ocorrências de uma palavra em uma string
# Searching the index of the frequency from the word in a string

string = 'Era uma vez um pudim apaixonado, estava andando nas ruas quando foi atrupelado, pff, pudim amassado, pudim amassadooo, pudem amassado dooo, pudim amassado morreu'.lower()
underline = '-'*15
positions = 0

while positions > -1:
    positions = string.find('pudim', positions)
    if positions > 0:
        print(f'{underline}\nPosition:  {positions}\n{underline}')
        positions += 1