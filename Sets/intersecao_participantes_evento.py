"""
Interseção de Participantes em Eventos.

Você está organizando dois eventos diferentes e tem listas de participantes para cada um. Quer saber quantas pessoas participaram de ambos os eventos.

Tarefas:
Crie duas listas de participantes para dois eventos diferentes.
Converta essas listas em conjuntos.
Use a operação de interseção para determinar o conjunto de todos os participantes que estiveram em ambos os eventos.
Imprima a lista de todos os participantes que estiveram em ambos os eventos e o número total desses participantes.
"""

# Storing players in lists
party_0 = ["Luan", "Pedro", "Joao", "Paula", "Amanda", "Rebeca", "Vanessa"]
party_1 = ["Luan", "Carlos", "Andre", "Ana", "Carolina", "Amanda", "Felipe", "Rebeca"]

# Converting the lists for sets
set_0 = set(party_0)
set_1 = set(party_1)

# Checking who go to the both parties
both_parties = set_0.intersection(set_1)

# Total participants
total_participants = len(both_parties)

print(f"Total participants number:{total_participants}\nList of the all participants: {both_parties}")