class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


ROOM1 = Room("ROOM1", None, 'ROOM3', 'ROOM2', None, "This is room 1 and there's an exit to the South"
                                                    " and East")
ROOM3 = Room("ROOM3", 'ROOM1', 'ROOM5', None, None, "This is room 3 and there's an exit to the South"
                                                    "You can go back North")
ROOM5 = Room("ROOM5", 'ROOM3', 'ROOM9', 'ROOM7', None, "This is room 5 and there's an exit to the South"
                                                       "There is also an exit to the East")
ROOM


#Option2

R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The parking Lot', None, "R19A")


