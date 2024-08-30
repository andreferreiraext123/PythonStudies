# Iterating with each element inside the tuple

import time
import threading
tupla = ("Andre", "Tiago", "Felipe", "Hiago", "Huan")

def repetico1(tupla):
    for element in tupla:
        print(element)


thred_repeticao_1 = threading.Thread(target=repetico1, args=(tupla,))
thred_repeticao_1.start()
thred_repeticao_1.join()
time.sleep(2)

print('\nPrimeiro for finalizado\n')


print('Iniciando a segunda thread!')

time.sleep(1)


def repeticaao_2(tupla):
    for element in tupla:
        print(element[0] + element[-1])

thred_repeticao_2 = threading.Thread(target=repeticaao_2, args=(tupla,))
thred_repeticao_2.start()
thred_repeticao_2.join

time.sleep(1)
print('As duas threads forma realizads com sucesso!')