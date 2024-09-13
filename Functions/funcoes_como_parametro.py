# Um ótimo recurso presento no python, é a capacidade de passar funcoes como parametros em outras funcao

def sum(num_1, num_2):
    return num_1 + num_2

def subtraction(num_1, num_2):
    return num_1 - num_2

def show(num_1, num_2, foper):
    print(foper(num_1, num_2))

show(10, 20, sum) # Outputs: 30
show(10, 20, subtraction) # Outputs: -10