class Carrot(object):
    def __init__(self, power, distance=30, stick=False, orange=True):
        # These are things that a WaterGun has.
        # All of us these should be relevant to our program.
        self.power = power
        self.range = distance
        self.trigger = True
        self.duration_of_bunny = 5
        self.stick = stick
        self.color = orange

    def shoot(self, time):
        if self.trigger:
            if self.duration_of_bunny <= 0:
                print("There's no bunny's left")
            elif self.duration_of_bunny < time:
                print("You run out of bunny's after firing for %s seconds", self.duration_of_bunny)
                self.duration_of_bunny = 0
            else:
                print("You shoot for %s seconds" % time)
                self.duration_of_pressure -= time
        else:
            print("There's no trigger!")

    def carrot_resurrection(self):
        self.duration_of_bunny = 5
    print("bunny's have been resurrected")


my_carrot = Carrot(5.2, 40, True)
your_carrot = Carrot(1.0, 1, False)
wiebe_carrot = Carrot(5, 50, True)
yahir_carrot = Carrot(0.1)
