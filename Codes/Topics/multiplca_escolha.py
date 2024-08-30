# Quiz de múltipla escolha

pontos = 0  # Inicializa a variável pontos com 0
questao = 1  # Inicializa a variável questao com 1

# Loop para iterar pelas questões do quiz
while questao <= 3:
    resposta = input(f"Resposta da questao {questao}: ")  # Solicita a resposta do usuário para a questão atual
    if questao == 1 and resposta == "b":  # Verifica se a questão é 1 e a resposta é "b"
        pontos = pontos + 1  # Se a resposta estiver correta, incrementa pontos
    if questao == 2 and resposta == "a":  # Verifica se a questão é 2 e a resposta é "a"
        pontos = pontos + 1  # Se a resposta estiver correta, incrementa pontos
    if questao == 3 and resposta == "d":  # Verifica se a questão é 3 e a resposta é "d"
        pontos = pontos + 1  # Se a resposta estiver correta, incrementa pontos
    questao = questao + 1  # Passa para a próxima questão
    
print(f"O aluno fez {pontos} ponto(s)")  # Exibe a pontuação final do aluno
