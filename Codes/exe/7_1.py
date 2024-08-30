# Escreva um programa que leia duas strings
    # Verifique se a segunda ocorre dentro da primeira. E aposiçao de ínicio.

string_0 = 'AABBEFAATT'
string_1 = 'BE'

if string_1 in string_0:
    print(string_0.find(string_1))
else:
    print('Nao há essa string!')