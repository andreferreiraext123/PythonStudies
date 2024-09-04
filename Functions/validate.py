def validador(minimo, maximo):
    while True:
        try:
            number = int(input("Enter the number: "))
            if number < minimo or number > maximo:
                print(f"Entre com um número válido! Entre {minimo} e {maximo}.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")
    return number

print(validador(1,10))