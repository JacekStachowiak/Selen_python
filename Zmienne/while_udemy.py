x = 0

while x < 10:
    print(f'Wartosc x to: {x}')
    x += 1
print('-------------------')
l = []    
num = 0

while num < 10:
    l.append(num)
    print(f'Wartosc num to: {num}')
    num += 1

print(l) 

y = 0
while y < 10:
    print(f'Wartosc y to: {y}')
    y += 1
    if y % 2 == 0:
        print(f'Parzyste: {y}')
print('======================')
y = 0
while y < 10:
    print(f'Wartosc y to: {y}')
    y += 1
    if y == 6:
        print(f'y = {y}')
        continue

print('======================')
y = 0
x = 0
while y < 10:
    print(f'y = {y}, x = {x}')
    y += 1
    while x < 10:
        print(f'x = {x}, y = {y}')
        x += 1
print('----------------------')
my_string = 'abcabc'
for s in my_string:
    if s == 'a':
        print('A', end=' ')
    else:
        print(s, end=' ')
    
cars = ['Audi', 'BMW', 'VW']
for car in cars:
    print(car, end='  ')

num_2 = [1,2,3]
for n in num_2:
    print(n * 10)

print('======================')    
d = {'one':1, 'two':2, 'tree':3}
for k in d:
    print(k+' '+str(d[k]))     

print('--------------')    
for k, v in d.items():
    print(f'k = {k}, v = {v}')