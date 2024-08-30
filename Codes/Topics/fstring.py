# É possível formarta os valores anexados aos f-strings

price = 5.20
# Alterando as opsiçoes, quantidade de caracteres exibidos
print(f'Preço:  {price:.2f}')
print(f'Preço:  {price:10.2f}')
print(f'Preço:  R${price:10.2f}')
print(f'Preço:  R${price:.2f}')

# Utilizando <,>e ^ para alinha os valores á direita, esquerda e ao centro
print(f'Preço: R${price:>10.2f}')
print(f'Preço:  R${price:<10.2f}')
print(f'Preço:  R${price:^10.2f}')

#E Até mesmo especificar os caracteres que preecheram os espaços em branco
print(f'Preço:  R${price:a<10.2f}')
print(f'Preço:  R${price:x<10.2f}')
print(f'Preço:  R${price:_^10.2f}')

# Chamando funcoes na f-string
print(f'Preço Inteiro:  R${int(price)}')

# Operaçoes matematicas na f-string
print(f'Preço + Imposto: R${price + (price * 0.1):.2f}')


# Usando aspas multiplas na f-string
print(f"""
... O preço do novo produto é:   R${price:5.2f}
... E pode ser encontrado nas melhores lojas do ramo
""")

# Utilizando quebradores de linha
quebra = "Primeira Linha\nSegunda Linha\nTerceira linha"
print(quebra)