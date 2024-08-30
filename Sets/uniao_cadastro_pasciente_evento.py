"""
Cadastro de Participantes de Eventos.

Você está organizando dois eventos diferentes e tem listas de participantes para cada um. Quer saber quantas pessoas distintas participaram de pelo menos um dos eventos.

Tarefas:
Crie duas listas de participantes para dois eventos diferentes.
Converta essas listas em conjuntos.
Use a operação de união para determinar o conjunto de todos os participantes únicos.
Imprima a lista de todos os participantes únicos e o número total de participantes distintos.
"""
# Storing the party's list
party_0 = ["André", "Luiz", "Dennis", "Joao", "Pedro"]
party_1 = ["André", "Mauricio", "Jacaiba", "Joao", "Gabriel", "Penelopi"]

# Converting from lists for sets
set_0 = set(party_0)
set_1 = set(party_1)

# Cheecking the total people and the people's name
union = set_0 | set_1
total_people = len(union)

# Priting
print(f"Total Players: {total_people}\nPlayers: {union}")