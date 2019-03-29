class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description="", items=None, characters=None):
        if items is None:
            items = []
        if characters is None:
            characters = []
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description
        self.items = items
        self.characters = characters


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
    def __init__(self, name):
        super(GoldSword, self). __init__(name, "gold", 20, "It inflicts 20 damage", 2, "medium")


class IronSword(Sword):
    def __init__(self, name):
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
    def __init__(self, name):
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


class Character(object):
    def __init__(self, name, health, weapon, armor, inventory, new_location):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.inventory = inventory
        self.current_location = new_location

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location

    def print_inventory(self):
        for item in self.inventory:
            print(item.name)


ROOM1 = Room("ROOM1", None, 'ROOM3', 'ROOM2', None, "This is room 1 and there's an exit to the South"
                                                    " and East. There is a stone sword.", ['StoneSword'], [])
ROOM3 = Room("ROOM3", 'ROOM1', 'ROOM5', None, None, "This is room 3 and there's an exit to the South."
                                                    " You can go back North", [], [])
ROOM5 = Room("ROOM5", 'ROOM3', 'ROOM9', 'ROOM7', None, "This is room 5 and there's an exit to the South."
                                                       " There is also an exit to the East", [HealthPotionLvl1], [None])
ROOM9 = Room("ROOM9", 'ROOM5', 'ROOM10', 'ROOM8', None, "This is room 9 and there's an exit to the South and East.",
                                                        [], [])
ROOM10 = Room("ROOM10", 'ROOM9', None, 'ROOM11', None, " This is room 10 and there's an exit to the North and East.")
ROOM2 = Room("ROOM2", None, 'ROOM7', None, 'ROOM1', "This is room 2 and there's an exit to the West and South.")
ROOM7 = Room("ROOM2", 'ROOM2', 'ROOM8', None, 'ROOM 5', "This is room 7 and there's an exit to the North, West,"
                                                        " and South")
ROOM8 = Room("ROOM8", 'ROOM7', None, None, 'ROOM9', "This is room 8 and there's an exit to the West and North.")
ROOM11 = Room("ROOM11", 'ROOM12', None, None, 'ROOM10', "This is room 11 and there's an exit to the North and West.")
ROOM12 = Room("ROOM12", None, 'ROOM11', 'ROOM13', None, "This is room 12 and there's an exit to the East and South.")
ROOM13 = Room("ROOM13", 'ROOM14', None, None, 'ROOM12', "This is room 13 and there's an exit to the North and West.")
ROOM14 = Room("ROOM14", 'EXIT', None, 'ROOM13', 'None', "This is room 14 and there's an exit to the North and East.")
EXIT = Room("EXIT ROOM", None, None, None, None, "CONGRATS YOU WIN!!", [], [])

# Players
player = Character("Jordan", 100, None, None, [], ROOM1)
playing = True
while playing:
    if len(player.current_location.items) > 0:
        for item in player.current_location.items:
            print("There is an item in this room")

    if len(player.current_location.characters) > 0:
        print("There is someone in this room")

    pickup = input("Would you like to pick up this item?")
    if pickup == "yes":
        player.inventory = player.inventory + player.current_location.items
        player.print_inventory()

@staticmethod
def pick_up_item():
        print("Your inventory is empty, make it full by getting items.")


directions = ['north', 'south', 'east', 'west', 'up', 'down']


# Items
StoneSword = StoneSword("Stone Sword")
IronSword = IronSword("Iron Sword")

# Characters
EvilJordan = Character("You", 100, SatansSword, None, None, None)

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
