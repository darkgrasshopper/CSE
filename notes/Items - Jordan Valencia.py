class Item(object):
            def __init__(self, name, material):
                self.name = name
                self.material = material


class Weapons(Item):
                def __init__(self, name, material, sword, shield, bow):
                    super(Item, self).__init__(name, material)
                    self.sword = sword
                    self.shield = shield
                    self.bow = bow


class Consumables(Item):
                    def __init__(self, name, heal, description):
                        super(Consumables, self).__init__(name)
                        self.heal = heal
                        self.description = description


class HealthPotionLvl1(Consumables):
                        def __init__(self, name, heal, description):
                            super(HealthPotionLvl1, self).__init__(name, heal, description)
                            self.heal = 10
                            self.description = "it healths 10 health"


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
        self.description = description


class StoneSword(Sword):
    def __init__(self, name, material, damage, description, duration, length):
        super(StoneSword, self).__init__(name, material, damage, description, duration, length)
        self.damage = 10
        self.description = "It inflicts 10 damage"
        self.duration = 1
        self.length = "medium"


class GoldSword(Sword):
    def __init__(self, name, material, damage, description, duration, length):
        super(GoldSword, self). __init__(name, material, damage, description, duration, length)
        self.damage = 20
        self.description = "It inflicts 20 damage"
        self.duration = 2
        self.length = "medium"


class IronSword(Sword):
    def __init__(self, name, material, damage, description, duration, length):
        super(IronSword, self).__init__(name, material, damage, description, duration, length)
        self.damage = 30
        self.description = "It inflicts 30 damage"
        self.duration = 2.5
        self.length = "long"

