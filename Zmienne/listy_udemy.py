cars = ['bmw', 'audi', 'honda']
pusta_lista = []
print(cars)
print(pusta_lista)

print('*#'*20)  # *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
print(cars[0]) # bmw
print(cars[1]) # audi
print('*'*20)
num_list = [1,2,3]
sum_list = num_list[1] + num_list[2]
print(sum_list) # 5

cars2 = ['bmw', 'audi', 'honda']
cars2[0] = 'Benz'
print(cars2)
print(cars2[0])

lenght = len(cars)
print(lenght) #3
cars.append('Benz')
print(cars)
cars.insert(1, 'Jeep') # dopisany na 2 pozycji
print(cars)
x = cars.index('audi')
print(x) #2
y = cars.pop()
print(y)
print(cars)
cars.remove('Jeep') # usunięty Jeep
print(cars)
print('='*20)
z = cars[1:]
print(z)
z = cars[0:2]
print(z)
z = cars[1:len(cars)]
print(z)
cars = ['bmw', 'audi', 'honda']
print(cars.sort()) # None
cars.sort()
print(cars) # ['audi', 'bmw', 'honda']
print('===================')


