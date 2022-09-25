
class Car(object):
    
    wheels = 4
    
    def __init__(self, marka, color, model = '550i'):
        self.marka=marka
        self.model=model
        self.color=color
        
    def info(self):
        print(f'Marka samochodu: {self.marka}')        
        print(f'Kolor samochodu: {self.color}')        
        print(f'Model samochodu: {self.model}')        

print(f'Liczba kół: {Car.wheels}')
print('---------------')

c1 = Car('Audi', 'black', 'A8')
c1.info()
print(c1.wheels)
c1.wheels = 3
print(c1.wheels)
# print(c1.marka)
# print(c1.model)

print('-------------')

c2 = Car('BMW', 'yellow')
c2.info()
print(c2.wheels)
# print(c2.marka)        
# print(c2.model)     
print('-------------------')   
print(f'Liczba kół: {Car.wheels}')