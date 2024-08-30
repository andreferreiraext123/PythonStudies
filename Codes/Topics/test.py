class Operations:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def sum(self):
        return self.num_1 + self.num_2
    
sum_ = Operations(10,10)
print(sum(sum_))