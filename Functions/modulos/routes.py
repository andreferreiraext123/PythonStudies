def valida_inteio(mensagem, minino, maximo):
    while True:
        #x += 1
        try:
            v = int(input(mensagem))
            if v >= minino or v <= maximo:
                return v
            else:
                print(f"Digite um valor entre {minino} e {maximo}")
        except ValueError as value:
            print(value)
            print("Soment número interiros!")
        #x += 1    