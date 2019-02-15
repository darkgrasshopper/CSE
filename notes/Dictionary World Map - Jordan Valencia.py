world_map = {
    'ROOM 1': {
        'NAME': "ROOM 1",
        'DESCRIPTION': "This is the room that you are in right now. "
                       "There is one exit to the South and East.",
        'PATHS': {
            'SOUTH': "ROOM 3",
            'EAST': "ROOM 2",
        }


    },
    "ROOM 3": {
        'NAME': "This is room 3 ",
        'DESCRIPTION': "There is a drawer, and a queen sized bed." 
                       "There is an exit to the south and north",
        'PATHS': {
            'SOUTH': "PATHWAY",
            'NORTH': "ROOM 1",
        }
    },
    "PATHWAY": {
        'NAME': "This is a pathway",
        'DESCRIPTION': "There is an exit to the south and north",
        'PATHS': {
            'SOUTH': "ROOM 5",
            'NORTH': "ROOM 3",
        }
    },
    "ROOM 2": {
        'NAME': "This is room 2",
        'DESCRIPTION': "There is an exit to the south and west",
        'PATHS': {
            'SOUTH': "HALLWAY",
            'WEST': "ROOM 1",
        }

    },
    "ROOM 7": {
        'NAME': "This is room 7",
        'DESCRIPTION': "There is an exit to the west, and to the south",
        'PATHS': {
            'WEST': "ROOM 5",
            'SOUTH': "ROOM 8",
        }
    },
    "ROOM 5": {
        'NAME': "This is room 5",
        'DESCRIPTION': "There is an exit to the North,South, and East",
        'PATHS': {
            'NORTH': "ROOM 3",
            'SOUTH': "ROOM 9",
            'EAST': "ROOM 7",
        }
    },
    "ROOM 9": {
        'NAME': "This is room 9",
        'DESCRIPTION': "There is an exit to the North, South, and East",
        'PATHS': {
            'NORTH': "ROOM 5",
            'SOUTH': "ROOM 10",
            'EAST': "ROOM 8",
        }
    },
    "ROOM 8": {}





}


#OtherVariables
current_node = world_map["ROOM 1"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

#Controller
while playing:
    print(current_node["NAME"])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way"),
else:
    print("Command not recognized")
