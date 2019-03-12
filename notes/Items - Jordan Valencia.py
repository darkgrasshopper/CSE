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
        self.description = "it heals you 10 health"


class HealthPotionLvl2(Consumables):
    def __init__(self, name, heal, description):
        super(HealthPotionLvl2, self).__init__(name, heal, description)
        self.heal = 15
        self.description = "it heals you 15 health"


class HealthPotionLvl3(Consumables):
    def __init__(self, name, heal, description):
        super(HealthPotionLvl3, self).__init__(name, heal, description)
        self.heal = 20
        self.description = "it heals you 20 health"


class Sword(Weapons):
    def __init__(self, name, material, damage, description, duration, length):
        super(Sword, self).__init__(name, material)
        self.damage = damage
        self.description = description
        self.duration = duration
        self.length = length


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


class SatansSword(Sword):
    def __init__(self, name, material, damage, description, duration, length):
        super(SatansSword, self).__init__(name, material, damage, description, duration, length)
        self.damage = 30
        self.description = "It inflicts 55 damage"
        self.duration = 4.0
        self.length = "long"


class Shield(Weapons):
    def __init__(self, name, material, protection, description):
        super(Shield, self).__init__(name, material)
        self.protection = protection
        self.description = description


class WoodenShield(Shield):
    def __init__(self, name, material, protection, description):
        super(WoodenShield, self).__init__(name, material, protection, description)
        self.protection = 5
        self.description = "this shield offers 5 protection"


class SteelShield(Shield):
    def __init__(self, name, material, protection, description):
        super(SteelShield, self).__init__(name, material, protection, description)
        self.protection = 10
        self.description = "this shield offers 10 protection"


class GlassShield(Shield):
    def __init__(self, name, material, protection, description):
        super(GlassShield, self).__init__(name, material, protection, description)
        self.protection = 11
        self.description = "this shield offers 11 protection"


class GoldShield(Shield):
    def __init__(self, name, material, protection, description):
        super(GoldShield, self).__init__(name, material, protection, description)
        self.protection = 15
        self.description = "this shield offers 15 protection"


class DiamondShield(Shield):
    def __init__(self, name, material, protection, description):
        super(DiamondShield, self). __init__(name, material, protection, description)
        self.protection = 25
        self.description = "this shield offers 25 protection"
