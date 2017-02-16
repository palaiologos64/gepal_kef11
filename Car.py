class car:
    def __init__(self,make):
        self.make=make
        self.speed= 60

    def speed_up(self,speed):
        self.speed = speed
        print "I am driving at a speed ",self.speed, "Km/h"

    def turn(self):
        print "I am turning  ....."

car1 = car("Obel")
print car1
print car1.speed

