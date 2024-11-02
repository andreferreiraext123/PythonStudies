# Faca um programa que verifique os tipos dos elementos em uma lista

list_ = ['Andre', 18, 50.2, True, False, ['Andre', 'Tiago', 'Sonia', 'Mauro'], {'id': 123}]

for element in list_:
    print(f'Element: {element}, Type: {type(element)}')