lista = [1,3,2,5,2,1]
lista.sort()
print(f'Usando o método sort:   {lista}')

lista_0 = [1,3,2,5,2,1]
print(sorted(lista_0)) # Output: 1,1,2,2,3,5
print(lista_0) #Output: 1,3,2,5,2,1



# O método sort ordena os elementos da lista em ordem crescente, modificando a lista original diretamente. Após a execução de lista.sort(), a lista lista é alterada permanentemente e seus elementos são reorganizados.

# A função sorted, por outro lado, também ordena os elementos em ordem crescente, mas retorna uma nova lista ordenada, sem modificar a lista original. Portanto, sorted(lista_0) retorna uma nova lista ordenada, enquanto lista_0 permanece inalterada.