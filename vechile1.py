# -*- coding: utf-8 -*-
class Vechile:
     def __init__(self,color,price,speed,idioktitis):
        self.color=color
        self.price = price
        self.wheels=4
        self.speed = speed
        self.owner=idioktitis
        print self

     def accelerate (self, amount):
         self.speed = self.speed +amount

     def decelerate (self,amount):
         self.speed = self.speed-amount

     def Speed(self):
        return self.speed

     def emfStoixeia(self):
        print " Το χρώμα του αυτοκίντου είναι ",self.color
        print "Ανήκει στον ",self.owner
        print " the price ", self.price
        print " Ο αριθμός των τροχών του είναι ", self.wheels
        print self

     def neaTimh(self):
        nt = input ("δώσε νεα τιμή ")
        self.price = nt




v1 = Vechile("Κοκκινο",10000,80,"Δημητρίου ")

v1.emfStoixeia()
v1.accelerate(20)
print " Η ταχύτητα είναι ", v1.Speed()
v1.neaTimh()
v1.emfStoixeia()
v2 = Vechile("Πράσινο", 10000,80,"Παπαδόπουλο ")
v2.emfStoixeia()
v2.accelerate(30)
print " Η ταχύτητα είναι ", v2.Speed()
v2.emfStoixeia()
print v2

