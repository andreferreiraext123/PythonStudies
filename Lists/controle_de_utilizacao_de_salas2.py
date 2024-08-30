lugares_vago = [10, 2, 1, 3, 0]

while True:
    sala = int(input('(0 Sai:) '))
    if sala == 0:
        print('Fim')
        break
    if sala < 1 or sala > len(lugares_vago):
        print('Sala inválida!')
        continue
    
    if lugares_vago[sala - 1] == 0:
        print('Desculpe, sala lotada!')
        continue

    lugares = int(input(f'Quantos lugares você deseja? {lugares_vago[sala - 1]} disponíveis: '))
    
    if lugares > lugares_vago[sala - 1]:
        print('Esse número de lugares não está disponível!')
    elif lugares < 0:
        print('Número inválido')
    else:
        lugares_vago[sala - 1] -= lugares
        print(f'{lugares} lugares vendidos')

print('Utilização das salas:')
for sala, vagos in enumerate(lugares_vago):
    print(f'Sala {sala + 1} - {vagos} lugares vazios')
