# Escreva um programa que compare duas listas. Utilizando operaçoes com conjuntos, e imprima os resultados das operacoes
#Storing lists
lista_0 = ["Andre", "Pedro", "Ana", "Maria", "Juana"]
lista_1 = ["Andre", "Joaquim", "Pedro", "Felipe", "Dionis", "Marcos", "Rebeca"]

# Converting from lists to sets
set_0 = set(lista_0)
set_1 = set(lista_1)

# Operation: Return the common values between two lists
operation_0 = set_0.intersection(set_1)

# Operation: Return the values that just be inside in first set
operation_1 = set_0 - set_1

# Operation: Return the vlue that just be inside in second set
operation_2 = set_1 - set_0

# Operation: Return a list with elements no duplicates between lists
operation_3 = list(operation_1 | operation_2)


# Priting the operations
print(f"Return elements duplicates: {operation_0}\nReturn elements that just be in the fisrt set: {operation_1}\nReturn the values that just be inside the second set: {operation_2}\nReturn a list of all duplicates elements: {operation_3}")

