class Item(object):
            def __init__(self, name, material):
                self.name = name
                self.material = material


class Weapons(Item):
                def __init__(self, name, material, sword, shield, bow):
                    super(Item,self).__init__(name, material)
                    self.sword = sword
                    self.shield = shield
                    self.bow = bow


class Consumables(Item):
                    def __init__(self, name, material, health_potion, health_potion_lvl2, health_potion_lvl3):
                        super(Consumables, self).__init__(name, material)
                        self.health_potion = health_potion
                        self.health_potion_lvl2 = health_potion_lvl2
                        self.health_potion_lvl3 = health_potion_lvl3


class Sword(Weapons):
            def __init__(self, name, material, damage, description, duration, length):
                super(Sword, self).__init__(name, material)
                self.damage = damage
                self.description = description
                self.duration = duration
                self.length = length


class Shield(Weapons):
    def __init__(self, name, material, protection, description,):
        super(Shield, self).__init__(name, material)
        self.protection = protection
        self.description - description

    StoneSword = Sword("Stone Sword", "Stone", 10, "it inflicts 10 damage", 1, "medium")
    GoldSword = Sword("Gold Sword", "Gold", 20, "it inflicts 20 damage", 2, "medium")
    IronSword = Sword("Sword Sword", "Iron", 30, "it inflicts 30 damage", 2.5, "long")


class StoneSword(Sword):
    def __init__(self, name, material, damage, description, duration, length):
        super(StoneSword, self).__init__(name, material, damage, description, duration, length)
        self.damage = 10
        self.description = "it inflicts 10 damage"
        self.duration = 1
        self.length = "medium"


class GoldSword =