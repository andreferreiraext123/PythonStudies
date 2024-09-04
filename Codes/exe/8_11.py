def lenString(minimo,maximo):
    while True:
        try:
            string = str(input("Enter a some text: "))
            if len(string) < minimo or len(string) > maximo:
                print(f"Enter with a valiable string with the len between {minimo} and {maximo}")
            else:
                print("Correct!")
                break # If the number is correct
        except ValueError:
            print("Please, enter with a correct string")
    return string

print(lenString(1,10))