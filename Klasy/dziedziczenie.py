
class Car(object):
    
    def __init__(self):
        print('Utworzyłeś instancję dla Car')
    
    def drive(self):
        print('Start ...')        
    
    def stop(self):
        print('Stopped ...')

class BMW(Car):
    
    def __init__(self):
        Car.__init__(self)
        print('Utworzyłeś instancję dla BMW')
    
    def drive(self):
        super(BMW, self).drive()
        print('Kieruję teraz BMW ...')    
    
    def display(self):
        print('To jest display')            


c = Car()
c.drive()
c.stop()
#c.display() - nie można wywołać
print('-----------------')
b = BMW()
b.drive()
b.stop()
b.display()
print('----------------')

# Utwórz klasę Fruit i 3 metody init, odżywianie, ksztłat owoca

class Fruit(object):
    
    def __init__(self):
        print('Stworzyłem klasę Fruit')
    
    def odzyw(self):
        print('To jest odżywianie')
    
    def ksztalt(self):
        print('To są kształty owoców')
    
class Food(Fruit):
    
    def __init__(self):
        Fruit.__init__(self)
        print('Klasa Food')
    
    def dodatkowa(self):
        print('To jest klasa dodatkowa')            
    
    def ksztalt(self):
        super(Food, self).ksztalt()
        print('Jeszcze dodatkowy ksztalt')        

f = Fruit()
f.odzyw()
f.ksztalt()
print('-----------------')
ft = Food()  
ft.odzyw()
ft.dodatkowa()
ft.ksztalt()      