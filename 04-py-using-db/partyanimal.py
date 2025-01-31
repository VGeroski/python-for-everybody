class PartyAnimal:

    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

    def __del__(self):
        print("I am destructed", self.x)

an = PartyAnimal("Sally")

an.party() # self - PartyAnimal.party(an)
an.party()
an.party()

j = PartyAnimal("Jim")
j.party()
an.party()

print("Type", type(an))
print("Dir ", dir(an))
print("Type", type(an.x))
print("Type", type(an.party))

an = 42 # destructor will be called before variable is overriden
print("an contains", an)
