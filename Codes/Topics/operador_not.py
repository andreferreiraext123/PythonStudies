# Atribuindo variavel
alcolizado = False

# Aplicando a lógica do operador Lógico Not.
dirigir = not alcolizado

# Determinando a mensagem correta
if dirigir:
    mensagem = "Você pode dirigir" # Mensagem se o valor for verdadeiro
else:
    mensagem = "Não pode dirigir!" # Mensagem se o valor for falso
# Imprimindo resultado da lógica do operador Not
print(f"Pode dirigir? {mensagem}, {dirigir}")
