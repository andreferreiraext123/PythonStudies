def faixa(n, max = 0 , step = 1):
    s = n
    if max == 0:
        max = n
    while n >= 0:
        if max == 0:
            break
        max -= 1

        yield s
        s, n = n - step, n - step
        

#a = faixa(10)
a = list(faixa(10, 5, 2))

print(a)