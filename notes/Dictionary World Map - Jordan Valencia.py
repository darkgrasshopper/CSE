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
                       "The south is room 5",
        'PATHS': {
            'SOUTH': "ROOM 3"
        }
    },
    "PATHWAY": {
        'NAME': "This is a pathway",
        'DESCRIPTION': "There is an exit to the south",
        'PATHS': {}


    }





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
