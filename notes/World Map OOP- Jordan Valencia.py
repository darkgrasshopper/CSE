class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


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
    def __init__(self, name, material, efficacy, description):
        super(Tool, self).__init__(name, material)
        self.efficacy = efficacy
        self.description = description


class StoneShovel(Tool):
    def __init__(self, name, material, efficacy, description):
        super(StoneShovel, self). __init__(name, material, efficacy, description)
        self.efficacy = 5
        self.description = "this stone shovel helps you dig with a 5 effectivity"


class StonePickAxe(Tool):
    def __init__(self, name, material, efficacy, description):
        super(StonePickAxe, self). __init__(name, material, efficacy, description)
        self.efficacy = 5
        self.description = "this Stone PickAxe helps you mine with a 5 effectivity"


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


ROOM1 = Room("ROOM1", None, 'ROOM3', 'ROOM2', None, "This is room 1 and there's an exit to the South"
                                                    " and East")
ROOM3 = Room("ROOM3", 'ROOM1', 'ROOM5', None, None, "This is room 3 and there's an exit to the South."
                                                    " You can go back North")
ROOM5 = Room("ROOM5", 'ROOM3', 'ROOM9', 'ROOM7', None, "This is room 5 and there's an exit to the South."
                                                       " There is also an exit to the East")
ROOM9 = Room("ROOM9", 'ROOM5', 'ROOM10', 'ROOM8', None, "This is room 9 and there's an exit to the South and East.")
ROOM10 = Room("ROOM10", 'ROOM9', None, 'ROOM11', None, " This is room 10 and there's an exit to the North and East.")
ROOM2 = Room("ROOM2", None, 'ROOM7', None, 'ROOM1', "This is room 2 and there's an exit to the West and South.")
ROOM7 = Room("ROOM2", 'ROOM2', 'ROOM8', None, 'ROOM 5', "This is room 7 and there's an exit to the North, West,"
                                                        " and South")
ROOM8 = Room("ROOM8", 'ROOM7', None, None, 'ROOM9', "This is room 8 and there's an exit to the West and North.")
ROOM11 = Room("ROOM11", 'ROOM12', None, None, 'ROOM10', "This is room 11 and there's an exit to the North and West.")
ROOM12 = Room("ROOM12", None, 'ROOM11', 'ROOM13', None, "This is room 12 and there's an exit to the East and South.")
ROOM13 = Room("ROOM13", 'ROOM14', None, None, 'ROOM12', "This is room 13 and there's an exit to the North and West.")
ROOM14 = Room("ROOM14", 'EXIT', None, 'ROOM13', 'None', "This is room 14 and there's an exit to the North and East.")
EXIT = Room("EXIT ROOM", None, None, None, None, "CONGRATS YOU WIN!!")

# Players
player = Player(ROOM1)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

# Items
StoneSword = StoneSword("Stone Sword", "Stone", 10, "This sword has inflicted 10 damage", 1, "medium")
IronSword = IronSword("Iron Sword", "Stone", 30, "This sword has inflicted 30 damage", 2.5, "long")


# Characters
c1 = Character("Orc1", 100, StoneSword, None)
c2 = Character("Orc2", 100, IronSword, None)
c1.attack(c2)
c2.attack(c1)
player = Character("You", 100, SatansSword, None)

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    if player.current_location.name == ['EXIT']:
        print("YOU WIN!!!")
        quit(0)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            # command = 'north
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("this key does not exist.")
        except AttributeError:
            print("I can't go that way.")
else:
    print("Command not recognized")
