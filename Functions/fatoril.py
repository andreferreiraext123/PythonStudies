# Começa com dois números (0 and 1)
    # A soma dos dois números anteriores retornam o valor da próxima possíçao
        # (0,1) O próximo valor dessa sequencia será dois valores passados somados
            # (0,1) >>> (0,1,1) >>> (0,1,1,2)  >>> (0,1,1,2,3)

# n * (n-1) enquanto n >= 1


def fatorial(num):
    if num <= 1:
        return 1
    else:
        return num * fatorial(num-1)
                            # 2
                            # 1


# 3 x 2, 6 x 1
num = 3
print(fatorial(num)) 