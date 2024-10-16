import random
x = random.randint(1,10) # Gera um número inteiro aleatório entre (1 e 9)

print(f"Random number {x}")

while True:
    n = int(input("Enter a number between 1 and 10: "))
    if n == x:
        print("Correct answer!")
        break
    else:
        print("Try again!")