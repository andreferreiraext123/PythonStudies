def generator_fibonacci():
    p = 0
    s = 1
    while s < 10:
        yield s # checkpoint
        p,s = s,s + p

list_comprehension = [x for x in generator_fibonacci()]        

print(list_comprehension)