from Animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self._heart_chamber = [3, 4]
        self.eggs = "Yes"

    def seek_heat(self):
        print("It's chilly, where's the sun?")

    def use_venom(self):
        print("if i've got it i'm using it")

    def attract_mate_through_scent(self):
        print("time to throw on the eau de toilette")


# jeremy_the_reptile = Reptile()
#
# print(jeremy_the_reptile.eggs)
# print(jeremy_the_reptile.alive)
# jeremy_the_reptile.attract_mate_through_scent()
# jeremy_the_reptile.breathe()