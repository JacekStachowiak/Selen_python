car = {'name':'BMW', 'model':'550', 'year':2020}
print(car)
print(car['name']) # BMW
model = car['name']
print(model)
print('----------------')
d = {}
d['one'] = 1
print(d) #{'one': 1}
d['two'] = 2
print(d) # {'one': 1, 'two': 2}
sum = d['one'] + 8
print(sum) # 9
d['two'] = d['two'] + 8
print(d) # {'one': 1, 'two': 10}
d['two'] += 10
print(d) # {'one': 1, 'two': 20}

cars_2 = {'BMW':{'model':'M740', 'year': 2021}, 'benz':{'model':'S80', 'year': 2022}}
print(cars_2)
bmw_year = cars_2['BMW']['year']
print(bmw_year)
print(cars_2['benz']['model']) # S80

c1 = {'name':'Audi', 'model':'A8', 'year':2021}
c2 = {'BMW':{'model':'M740', 'year': 2021}, 'benz':{'model':'S80', 'year': 2020}}
print(c1.keys())
print(c2.keys())
print(c1.values())
print(c2.values())
print(c1.items())
print(c2.items())
print('-------------------')
car_copy = c1.copy()
car_copy2 = c2.copy()
print(car_copy)
print(car_copy2)
# car_copy.clear()
car_copy.pop('model')
print(car_copy)