class Item(object):
            def __init__(self, name, material):
                self.name = name
                self.material = material


class Weapons(Item):
                def __init__(self, sword, shield, bow):
                    self.sword = sword
                    self.shield = shield
                    self.bow = bow
                    

class Sword(Weapons):
            def __init__(self, name, material, damage, description, duration, length):
                super(Sword, self).__init__(name, material)
                self.damage = damage
                self.description = description
                self.duration = duration
                self.length = length


StoneSword = Sword("Stone Sword", "Stone", 10, "it inflicts 10 damage", 1, "medium")
GoldSword = Sword("Gold Sword", "Gold", 20, "it inflicts 20 damage", 2, "medium")
IronSword = Sword("Sword Sword", "Iron", 30, "it inflicts 30 damage", 2.5, "long")
