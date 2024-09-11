def checkingElements(estring,lista):
    for word in lista:
        if word == estring:
            return True
    else:
        return False

estring = input("Enter a string: ")
lista = ["Bom dia", "Oi", "Andre", "Matos", "Bds"]


print(checkingElements(estring,lista))