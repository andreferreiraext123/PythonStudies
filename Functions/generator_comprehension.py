list_ = [item for item in range(10) if item % 3 == 0]
print(list_)

dict_ = (item for item in range(10) if item % 3 == 0)
print(dict_)

for item in dict_:
    print(item)