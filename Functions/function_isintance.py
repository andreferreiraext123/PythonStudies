# Para verificar se o tipo da variavel equivale a outro tipo, utilizaremos a funcao isintance

import types # Importando o modulo types

def show_type(variable):
    if isinstance(variable, str):
        return f'{variable} String'
    elif isinstance(variable, int):
        return f'{variable} int'
    elif isinstance(variable, float):
        return f'{variable} Float'
    elif isinstance(variable, bool):
        return f'{variable} Boolean'
    elif isinstance(variable, dict):
        return f'{variable} Dictionary'
    elif isinstance(variable, list):
        return f'{variable} List'
    
print(show_type('Andre'))
print(show_type(18))
print(show_type(True))
print(show_type([1,2,3,5]))
print(show_type([10,20,[30,30]]))
print(show_type({'phone_number': 970611681}))

"""
Output:

Andre String
18 int
True int
[1, 2, 3, 5] List
[10, 20, [30, 30]] List
{'phone_number': 970611681} Dictionary
"""