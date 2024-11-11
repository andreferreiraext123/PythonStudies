list_ = [1,2,3]
iterator = iter(list_)
print(iterator) # Output: <list_iterator object at 0x7df063b4e440>

print(next(iterator)) # Output: 1
print(next(iterator)) # Output: 2
print(next(iterator)) # Output: 3

# Usando a funcao iteradora 'iter' para dicionarios

dic_ = {'Name': 'Andre', 'Age': 18}
interator_ = iter(dic_) # Output:

print(interator_)
print(next(interator_)) # Output: Andre
print(next(interator_)) # Output: 18

for values in dic_.values():
    print(values)