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
    def __init__(self, name, heal, poison, description):
        super(HealthPotionLvl1, self).__init__(name, heal, poison, description, None)
        self.heal = 10
        self.description = "it heals you 10 health"
        self.poison = None


class HealthPotionLvl2(Consumables):
    def __init__(self, name, heal, poison, description):
        super(HealthPotionLvl2, self).__init__(name, heal, poison, description, None)
        self.heal = 15
        self.description = "it heals you 15 health"
        self.poison = None


class HealthPotionLvl3(Consumables):
    def __init__(self, name, heal, poison, description):
        super(HealthPotionLvl3, self).__init__(name, heal, poison, description, None)
        self.heal = 20
        self.poison = None
        self.description = "it heals you 20 health"


class PoisonPotionLvl1(Consumables):
    def __init__(self, name, heal, poison, description):
        super(PoisonPotionLvl1, self).__init__(name, heal, poison, description, None)
        self.heal = None
        self.poison = 10
        self.description = "it takes away 10 health"


class PoisonPotionLvl2(Consumables):
    def __init__(self, name, heal, poison, description):
        super(PoisonPotionLvl2, self).__init__(name, heal, poison, description, None)
        self.heal = None
        self.poison = 15
        self.description = "it takes away 15 health"


class PoisonPotionLvl3(Consumables):
    def __init__(self, name, heal, poison, description):
        super(PoisonPotionLvl3, self).__init__(name, heal, poison, description, None)
        self.heal = None
        self.poison = 20
        self.description = "it takes away 20 health"


class Sword(Weapon):
    def __init__(self, name, material, damage, description, duration, length):
        super(Sword, self).__init__(name, damage, material)
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


class Shield(Weapon):
    def __init__(self, name, material, protection, description):
        super(Shield, self).__init__(name, None, material)
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


class Tool(Item):
    def __init__(self, name, material, effectivity, description):
        super(Tool, self).__init__(name, material)
        self.effectivity = effectivity
        self.description = description


class StoneShovel(Tool):
    def __init__(self, name, material, effectivity, description):
        super(StoneShovel, self). __init__(name, material, effectivity, description)
        self.effectivity = 5
        self.description = "this stone shovel helps you dig with a 5 effectivity"


class StonePickAxe(Tool):
    def __init__(self, name, material, effectivity, description):
        super(StonePickAxe, self). __init__(name, material, effectivity, description)
        self.effectivity = 5
        self.description = "this Stone PickAxe helps you mine with a 5 effectivity"
