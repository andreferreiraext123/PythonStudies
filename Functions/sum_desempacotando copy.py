def barra(n = 10, c = "*"):
    print(c * n) # "*" * 10

lista = [[5, "-"], [10, "*"], [5], [6, "."]] #0,1,2,3 elements

for element in lista:
    barra(*element) # print("*" * 5): Outputs: -----

'''
-----
**********
*****     
......    
'''