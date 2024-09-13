def sum(num_1,num_2, imprime= False):
    sum = num_1 + num_2
    # Se for verdadeiro a soma será impressa
    if imprime:
        print(sum)
    return sum

sum(10,20,True) # Com todos os parametros incluindo o opcional
sum(10,20) # Sem o parametro opcional