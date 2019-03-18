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
    def __init__(self, name, damage, material, protection):
        super(Weapon, self).__init__(name, material)
        self.damage = damage
        self.protection = protection


class Consumables(Item):
    def __init__(self, name, heal, description, material):
        super(Consumables, self).__init__(name, material)
        self.heal = heal
        self.description = description


class HealthPotionLvl3(Consumables):
    def __init__(self, name, heal, description):
        super(HealthPotionLvl3, self).__init__(name, heal, description, None)
        self.heal = 20
        self.description = "it heals you 20 health"


class Sword(Weapon):
    def __init__(self, name, material, damage, description, duration, length):
        super(Sword, self).__init__(name, damage, material)
        self.description = description
        self.duration = duration
        self.length = length


class Shield(Weapon):
    def __init__(self, name, material, protection, description):
        super(Shield, self).__init__(name, None, material)
        self.protection = protection
        self.description = description


sword = Weapon("Stone Sword", 10, "Stone", None)
sword2 = Weapon("Gold Sword", 20, "Gold", None)
sword3 = Weapon("Iron Sword", 30, "Iron", None)
sword4 = Weapon("Satans Sword", 30, "Obsidian", None)
shield = Weapon("Wooden Shield", None, "Wood", 5)
shield2 = Weapon("Steel Shield", None, "Steel", 10)
shield3 = Weapon("Glass Shield", None, "Glass", 11)
shield4 = Weapon("Gold Shield", None, "Gold Shield", 15)



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
sword = Weapon("Sword", 15, None)
sword2 = Weapon("Orc Sword", 5, None)


# Characters
c1 = Character("Orc1", 100, sword, None)
c2 = Character("Orc2", 100, sword2, None)
c1.attack(c2)
c2.attack(c1)


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
