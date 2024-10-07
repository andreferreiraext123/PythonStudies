# Quando criamos várias funcoes, é comum querermos utilizas em outros arquivos, a fim de reutilizar o código, bom isso é possível graça aos módulos
    # Módulos sao todo e qualuqer arquivo .py
# Os módulos sao capazes de armazenar as funcoes lá escritas e podendo ser utilzadas em outros arquivos

import routes # Aqui estamos importando o módeulo routes
from routes import valida_inteio # Aqui estamos importando uma funcao do módulo routes.py

lista = []

for x in range(10):
    lista.append(valida_inteio("Digite um número: ", 0, 20))
    print(f"Soma {sum(lista)}") # Aqui estamos imprimindo a soma de todos os elementos da lista 'lista'    