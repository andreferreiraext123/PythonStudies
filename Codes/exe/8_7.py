# Defina uma funcao recursiva que calcule o maior divisor comum (M.D.C), entre dois números (a e b)

def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Exemplo de uso
resultado = mdc(48, 18)
print("MDC:", resultado)