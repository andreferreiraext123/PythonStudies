# Rewrite the function from program 8.1 and reuse the list search methods shown in chapter 7

def search(list_,value):
    if value in list_:
        return list_.index(value)
    return None

list_ = [10, 20, 25, 30]

print(search(list_, 25))
print(search(list_, 27))