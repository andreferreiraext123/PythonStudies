# Podemos criar um número indeterminado de valores como parametro, basta empacotarmos e desempacotar

def sum(*numbers):
    total_sum = 0
    for element in numbers:
        total_sum += element
    return total_sum

print(sum(2,1,22,11,2))
