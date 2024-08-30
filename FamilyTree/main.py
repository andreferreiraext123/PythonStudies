class FamileMember:
    def __init__(self, name, age, height, weight, type):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.type = type

    def PrintInformations(self):
        print(f'Name:    {self.name}')
        print(f'Age:    {self.age}')
        print(f'Height: {self.height:.2f} CM')
        print(f'Weight: {self.weight:.2f} KG')
        print(f'Type:   {self.type}')

    def Hello(self):
        print("Hello, I'm a family member\n")