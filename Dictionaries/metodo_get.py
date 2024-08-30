dictionary = {}

for letter in "GoodMorning":
    dictionary[letter] = dictionary.get(letter, 0) + 1
    print(dictionary)