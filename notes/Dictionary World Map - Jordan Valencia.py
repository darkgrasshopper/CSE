world_map = {
    'R19A': {
        'NAME': "",
        'DESCRIPTION': "This is the classroom that you are in right now. "
                       "It has two exits to the north side.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }

    },
    "PARKING_LOT": {
        'NAME': "The Edison Parking Lot",
        'DESCRIPTION': "There are cars parked here." 
                       "The south is Mr.Wiebe's room",
        'PATHS': {
            'SOUTH': "R19A"
        }
    }
}
