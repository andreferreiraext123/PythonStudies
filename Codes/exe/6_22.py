"""
Crie um programa que compare duas listas
- Considere a primeira lista como a versao inicial e a segundo como a versao após as alteraçoes
- E liste:  
    - Os elementos que nao mudaram
    - os novos elementos
    - os elementos que foram removidos
""" 

lista_antes = [1,2,3,4,5,6]
lista_depois = [5,6,7,8,9,10]

set_antes = set(lista_antes)
set_depois = set(lista_depois)

# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print(f"Elementos que nao mudaram:  {set_antes & set_depois}")
print(f"Novos elementos:    {set_depois - set_antes}")
print(f"Elementos removidos:    {set_antes - set_depois}")

