poll = [
    "Hot",
    "Sunny",
    "Sunny",
    "Cold",
    "Cold",
    "Cold",
    "Hot",
    "Sunny",
    "Hot",
    "Cold"
]

def count_votes(poll):
    counter = {
        "Hot": 0,
        "Sunny": 0,
        "Cold": 0,
    }

    for answer in poll:
        if answer in counter:
            counter[answer] += 1

    # Encontrar a resposta mais votada e o número de votos
    max_vote = max(counter, key=counter.get)
    return [max_vote, counter[max_vote]]

result = count_votes(poll)
print(result)  # Saída: ['Cold', 4]