class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


ROOM1 = Room("ROOM1", None, 'ROOM3', 'ROOM2', None, "This is room 1 and there's an exit to the South"
                                                    " and East"),
ROOM3 = Room("ROOM3", 'ROOM1', 'ROOM5', None, None, "This is room 3 and there's an exit to the South"
                                                    "You can go back North"),
ROOM5 = Room("ROOM5", 'ROOM3', 'ROOM9', 'ROOM7', None, "This is room 5 and there's an exit to the South"
                                                       "There is also an exit to the East"),
ROOM9 = Room("ROOM9", 'ROOM5', 'ROOM10', 'ROOM8', None, "This is room 9 and there's an exit to the South and East"),

ROOM10 = Room("ROOM10", 'ROOM9', None, 'ROOM11', None, "This is room 10 and there's an exit to the North and East"),

ROOM2 = Room("ROOM2", None, 'ROOM7', None, 'ROOM1', "This is room 2 and there's an exit to the West and South"),

ROOM7 = Room("ROOM2", 'ROOM2', 'ROOM8', None, 'ROOM 5', "This is room 7 and there's an exit to the North, West,"
                                                        " and South"),
ROOM8 = Room("ROOM8", 'ROOM 7', None, None, 'ROOM9', "This is room 8 and there's an exit to the West and North"),

ROOM11 = Room("ROOM11", 'ROOM 12', None, None, 'ROOM10', "This is room 11 and there's an exit to the North and West"),

ROOM12 = Room("ROOM12", None, 'ROOM11', 'ROOM13', None, "This is room 12 and there's an exit to the East and South"),

ROOM13 = Room("ROOM13", 'ROOM14', None, None, 'ROOM12', "This is room 13 and there's an exit to the North and West"),

ROOM14 = Room("ROOM14", 'EXIT', None, 'ROOM13', 'None', "This is room 14 and there's an exit to the North and East"),

EXIT =




