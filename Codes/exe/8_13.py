def checkingOptionsInString(estring):
    while True:
        option = input("Enter a option:  ")

        estring = estring.lower()
        option = option.lower()
        quantityHits = 0
        
        for letter in estring:
            if letter == option:
                quantityHits += 1
                print(quantityHits)

        if quantityHits == len(estring):
                print("You got everything right")
                break    
        else:
            quantityHits = 0
            print("Try again!")

test = checkingOptionsInString("a")


