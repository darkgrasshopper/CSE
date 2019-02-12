class WaterGun(object):
      def __init__(self, capacity, distance, stock):
        # These are things that a WaterGun has.
        # All of us these should be relevant to our program.
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.duration_of_pressure = 5
        self.stock = stock


    def shoot(self, time):
        if self.trigger:
            if self.duration_of_pressure <= 0:
                print("There's no pressure")
        elif self.duration_of_pressure < time:
            print("You run out of pressure after firing for %s seconds", self.duration_of_pressure)
            self.duration_of_pressure = 0
    else:
 print("You shoot for %s seconds" % time)
        self.duration_of_pressure -= time
 print("There's no trigger!")

my_water_gun = WaterGun()

