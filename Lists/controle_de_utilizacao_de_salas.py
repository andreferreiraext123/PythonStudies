# Crie um programa que verifique a quantidade de lugares vazios em salas especificas.
# Caso a sala tenha disponível lugares permitir a venda de um lugar. E retornar mensagem adequades de acordo com a situacao de cada sala
# Lotada/Quantidade de lugares

# Data Storing
lugares_vagos = [10,2,5,0,1]# Cada índice representa a quantidade de lugares vazios em cada sala respectivamente (Sala 1, Sala 2,..)
quantity_tickets = 0

while True:
    sala = int(input('Which room do you want to buy a ticket? (Enter 0 if you want stop!): '))
    if sala == 0:
        print(f'Program Stoped!')
        break
    
    elif sala == 1:
        lugares_vagos[0] -= 1
        if lugares_vagos[0] <= 0:
            print('Room 1 empty')
    elif sala == 2:
        lugares_vagos[1] -= 1
        if lugares_vagos[1] <= 0:
            print('Room 2 empty')
    elif sala == 3:
        lugares_vagos[2] -= 1
        if lugares_vagos[2] <= 0:
            print('Room 3 empty')
    elif sala == 4:
        lugares_vagos[3] -= 1
        if lugares_vagos[3] <= 0:
            print('Room 4 empty')
    elif sala == 5:
        lugares_vagos[4] -= 1
        if lugares_vagos[4] <= 0:
            print('Room 5 empty')

    else:
        print('Invalid Room! Please, enter with the correct number room!')

    quantity_tickets = quantity_tickets + 1

print(f'Number of tickets purchased: {quantity_tickets}')
print(f'Rooms:  {lugares_vagos}')


    