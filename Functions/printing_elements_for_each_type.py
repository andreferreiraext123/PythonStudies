# Faca um programa que imprima elemetos de acordo com o seu tipo

import types

def show_string_elements(list_):
    for element in list_:
        if isinstance(element, str):
            print(f'Element {element}, Type {type(element)}')

def show_int_elements(list_):
    for element in list_:
        if isinstance(element, int):
            print(f'Element {element}, Type {type(element)}')

list_ = ['Andre', 'Tiago', 19, [2,1312, '32'], {'id': 123}]

show_string_elements(list_)
show_int_elements(list_)

#for element in list_:
#    if isinstance(element, str): # Only print element that is equal than string type
#        print(element)