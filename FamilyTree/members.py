from main import FamileMember

class Friends(FamileMember):
    pass

    def Hello(self):
        print("Hello, I'm a friend\n")


luiz = Friends('Luiz', 18, 1.70, 70, 'Friend')
luiz.PrintInformations()
luiz.Hello()

sonia = FamileMember('Sonia', 40, 1.60, 65, 'Mother')
sonia.PrintInformations()
sonia.Hello()

mauro = FamileMember('Mauro', 51, 1.62, 75, 'Father')
mauro.PrintInformations()
mauro.Hello()

tiago = FamileMember('Tiago', 22, 1.68, 78, 'Brother')
tiago.PrintInformations()
tiago.Hello()

andre = FamileMember('Andre', 18, 1.70, 60, 'Son')
andre.PrintInformations()
andre.Hello()