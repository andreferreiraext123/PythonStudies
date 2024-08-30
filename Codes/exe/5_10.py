# Quiz de multiplca escolha

# Iniciando variaveis
pontos = 0 # Iniciando contador de pontos
questao = 1 # Identifacador do número da questao

# Imprimindo opçoes de respostas
print("Resposta:    D")
print("Resposta:    A")
print("Resposta:    B")

# Loop para interar com as questoes do quiz
while questao <= 3: # Verificando se o número da questao é igual o menor que 3
    resposta = str(input(f"Escolha a resposta da questao {questao}:  ")) # Resposta da questao do usuário

    if questao == 1 and resposta == "b" or resposta == "B": # Questao um
        pontos = pontos + 1 # Acumulo de pontos se a questao 1 estiver correta

    if questao == 2 and resposta == "a" or resposta == "A": # Questao dois
        pontos = pontos + 1 # Acumulo de pontos se a questao 2 estiver correta
    
    if questao == 3 and resposta == "d" or resposta == "D": # Questao tres
        pontos = pontos + 1 # Acumulo de pontos se a questao 3 estiver correta
    questao = questao + 1

print(f"O aluno fez {pontos} ponto(s)") # Imprimindo pontuaçao
