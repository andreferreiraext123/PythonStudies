# Definindo variáveis lógicas (booleanas)
esta_chovendo = True
tem_guarda_chuva = False

# Verificando condições e tomando decisões com base nas variáveis lógicas
if esta_chovendo:
    if tem_guarda_chuva:
        print("Está chovendo, mas você tem um guarda-chuva. Pode sair!")
    else:
        print("Está chovendo e você não tem um guarda-chuva. Melhor ficar em casa.")
else:
    print("Não está chovendo. Você pode sair sem problemas!")

# Outro exemplo usando variáveis lógicas
tem_dinheiro = True
banco_aberto = True

# Verificando se pode ir ao banco
if tem_dinheiro and banco_aberto:
    print("Você pode ir ao banco depositar o dinheiro.")
elif not tem_dinheiro:
    print("Você não tem dinheiro para depositar.")
elif not banco_aberto:
    print("O banco está fechado, não pode fazer o depósito agora.")
