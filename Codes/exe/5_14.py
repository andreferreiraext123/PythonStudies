# Armazenando váriaveis
soma = 0
media = 0
quantidade = 0

while True:
    number = int((input("Digite números para o calcule. E caso queria interromper digite (0):   ")))
    if number == 0:
        break
    quantidade += 1
    soma += number
    media = soma / quantidade
     

print(f"Soma dos valores:   {soma}")
print(f"Quantidade de valores digitados:    {quantidade}")
print(f"Media aritimética dos valores:  {media}")