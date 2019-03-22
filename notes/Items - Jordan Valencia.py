class Item(object):
    def __init__(self, name, material):
        self.name = name
        self.material = material


class Weapon(Item):
    def __init__(self, name, damage, material,):
        super(Weapon, self).__init__(name, material)
        self.damage = damage


class Consumables(Item):
    def __init__(self, name, heal, poison, description, material):
        super(Consumables, self).__init__(name, material)
        self.heal = heal
        self.description = description
        self.poison = poison


class HealthPotionLvl1(Consumables):
    def __init__(self, name):
        super(HealthPotionLvl1, self).__init__(name, 10, None, "it heals you 10 health", None)


class HealthPotionLvl2(Consumables):
    def __init__(self, name):
        super(HealthPotionLvl2, self).__init__(name, 15, None, "it heals you 15 health", None)


class HealthPotionLvl3(Consumables):
    def __init__(self, name):
        super(HealthPotionLvl3, self).__init__(name, 20, None, "it heals you 20 health", None)


class PoisonPotionLvl1(Consumables):
    def __init__(self, name):
        super(PoisonPotionLvl1, self).__init__(name, None, 10, "it takes away 10 health", None)


class PoisonPotionLvl2(Consumables):
    def __init__(self, name):
        super(PoisonPotionLvl2, self).__init__(name, None, 15, "it takes away 15 health", None)


class PoisonPotionLvl3(Consumables):
    def __init__(self, name):
        super(PoisonPotionLvl3, self).__init__(name, None, 20, "it takes away 20 health", None)


class Sword(Weapon):
    def __init__(self, name, material, damage, description, duration, length):
        super(Sword, self).__init__(name, damage, material)
        self.description = description
        self.duration = duration
        self.length = length


class StoneSword(Sword):
    def __init__(self, name):
        super(StoneSword, self).__init__(name, "stone", 10, "It inflicts 10 damage", 1, "medium")


class GoldSword(Sword):
    def __init__(self, name, material, damage, description, duration, length):
        super(GoldSword, self). __init__(name, "gold", 20, "It inflicts 20 damage", 2, "medium")


class IronSword(Sword):
    def __init__(self, name, material, damage, description, duration, length):
        super(IronSword, self).__init__(name, "iron", 30, "It inflicts 30 damage", 2.5, "long")


class SatansSword(Sword):
    def __init__(self, name):
        super(SatansSword, self).__init__(name, "obsidian", 30, "It inflicts 55 damage", 4.0, "long")


class Shield(Weapon):
    def __init__(self, name, material, protection, description):
        super(Shield, self).__init__(name, None, material)
        self.protection = protection
        self.description = description


class WoodenShield(Shield):
    def __init__(self, name):
        super(WoodenShield, self).__init__(name, "wood", 5, "this shield offers 5 protection")


class SteelShield(Shield):
    def __init__(self, name):
        super(SteelShield, self).__init__(name, "steel", 10, "this shield offers 10 protection")


class GlassShield(Shield):
    def __init__(self, name, material, protection, description):
        super(GlassShield, self).__init__(name, "glass", 11, "this shield offers 11 protection")


class GoldShield(Shield):
    def __init__(self, name):
        super(GoldShield, self).__init__(name, "gold", 15, "this shield offers 15 protection")


class DiamondShield(Shield):
    def __init__(self, name):
        super(DiamondShield, self). __init__(name, "diamond", 25, "this shield offers 25 protection")


class Tool(Item):
    def __init__(self, name, material, efficacy, description):
        super(Tool, self).__init__(name, material)
        self.efficacy = efficacy
        self.description = description


class StoneShovel(Tool):
    def __init__(self, name):
        super(StoneShovel, self). __init__(name, "stone", 5, "this stone shovel helps you dig with a 5 effectivity")


class StonePickAxe(Tool):
    def __init__(self, name):
        super(StonePickAxe, self). __init__(name, "stone", 5, "this Stone PickAxe helps you mine with a 5 effectivity")