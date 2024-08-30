# Solicita ao usuário os dois números
primeiro_numero = int(input("Digite o primeiro número para a divisão: "))
segundo_numero = int(input("Digite o segundo número para a divisão: "))

# Inicializa as variáveis para o quociente e o resto
quociente = 0
resto = primeiro_numero

# Calcula o quociente usando apenas subtração e adição
while resto >= segundo_numero:
    resto = resto - segundo_numero  # Subtrai o divisor (segundo_numero) do resto
    quociente = quociente + 1      # Incrementa o contador (quociente)

# Imprime os resultados
print(f"Quociente da divisão de {primeiro_numero} por {segundo_numero} é: {quociente}")
print(f"Resto da divisão de {primeiro_numero} por {segundo_numero} é: {resto}")
