# -*- coding: utf-8 -*-
class Vechile(object):
     def __init__(self,color,price,speed,idioktitis):
        self.color=color
        self.price = price
        self.wheels=4
        self.speed = speed
        self.owner=idioktitis

     def accelerate (self, amount):
         self.speed = self.speed +amount

     def decelerate (self,amount):
         self.speed = self.speed-amount

     def Speed(self):
        return self.speed

     def __str__(self):
        rstr = "Το όχημα ανήκει στον " +self.owner +"\n" +"η τιμή του είναι " +str(self.price)
        return rstr
v1 = Vechile("Κοκκινο",10000,80,"Δημητρίου ")
print v1
print type(v1)
print dir(v1)