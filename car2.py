# -*- coding: utf-8 -*-
class car:
    def __init__(self,make,color,etos):
        self.make=make
        self.speed = 60
        self.color = color
        self.year = etos

    def speed_up(self,speed):
        self.speed = speed
        print "I am driving at a speed ",str(self.speed), "Km/h"

    def turn(self,strofe):
        print "I am turning  .....",strofe

convertible = car("bmw","Black",2013)
sedan=car("toyota","red",2009)
convertible.turn("Δεξια")
convertible.speed_up(90)



