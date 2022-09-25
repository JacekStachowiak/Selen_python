import math
from math import sqrt
#import Klasy.klasy_1 as car
from Klasy.klasy_1 import Car

class Modules():
    
    def modul_1(self):
        print(math.sqrt(100))
        print(sqrt(900))
    
    def car_description(self):
        marka = 'BMW'
        model = '550i'
        Car(marka, model)
                

m = Modules()
m.modul_1() 
m.car_description()       

