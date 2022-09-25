
def sum_num(a,b):
    'To funkcja sumująca'
    return a + b

print(sum_num(3,5)) 

l = [1,2,3]
l.append(4)
print(len(l))
print(l)
print('---------------')

def sum_num_2(a=2,b=4):
    'To funkcja sumująca'
    return a + b

print(sum_num_2())  # 6
print(sum_num_2(4,4)) # 8
print(sum_num_2(a=5,b=5)) # 10
print(sum_num_2(5)) # 9
print(sum_num_2(b=10)) # 12

print('---------------')

def isMetro(city):
    'Stolice które mają metro'
    l = ['New York', 'Los Angeles', 'Washington']
    if city in l:
        return True
    else:
        return False
    
x = isMetro('New York')    
print(x)
y = isMetro('Boston')
print(y)

print(sum_num.__doc__)  # To funkcja sumująca
print(isMetro.__doc__)  # Stolice które mają metro
print('-----------------')

a = 10
def test_method(a):
    print(f'Wartość lokalna a = {a}')
    a = 2
    print(f'Wartość lokalna a = {a}')

print(f'Wartość globalna a to {a}') # 10
test_method(a)  # 2

print('=======================')

a = 10
def test_method():  # usuwamy z parametrów
    global a
    print(f'Wartość lokalna a = {a}') # 10  
    a = 2
    print(f'Wartość lokalna a = {a}') # 2

print(f'Wartość globalna a to {a}') # 10
test_method()  

# min(), max(), abs(), type()

def largest_num(*args): # dowolna liczba argumentów
    print(max(args))
    return max(args)    

def minimum_num(*args):
    #print(min(args))
    return min(args)

def abs_num(a): # wartość bezwzględna
    print(abs(a))
    return abs(a)

def type_symbol(x):
    print(type(x))

largest_num(-20, -10, 5, 15)   # 15
minimum_num(-20, -10, 5, 15)   # -20
x = minimum_num(-20, -10, 5,15) 
print(x)    # -20

abs_num(-20)    # 20
abs_num(20)     # 20

print('==================')
print(type(99))     # <class 'int'>
print(type(99.9))   # <class 'float'>
print(type('99'))   # <class 'str'>
l = [1,2,3]
print(type(l))      # <class 'list'>

print('---------------------') # def type_symbol
type_symbol(99)
type_symbol(99.9)
type_symbol('99')
type_symbol(l)

# zadanie oblicz podatek - powiedzmy dla dochodu 0 - 50000 - 19%, 50000-100000  - 25%, od 100000 - 30%

def podatek(d):
    if d <= 50000:
        p = d * 0.19
        pl = d-p
        print(f'Podatek wynosi {p}')
        print(f'Na rękę dostaniesz {pl}')
    elif d > 50000 and d <= 100000:
        p = d * 0.25
        pl = d-p
        print(f'Podatek wynosi {p}') 
        print(f'Na rękę dostaniesz {pl}')       
    else:
        p = d * 0.30
        pl = d-p
        print(f'Podatek wynosi {p}')
        print(f'Na rękę dostaniesz {pl}')        

print('------------------')
podatek(35000)        

# 3 regiony w Polsce A - 19%, B - 25%, C - 30% i inne podatki

s = {'A':0.19, 'B':0.25, 'C':0.30}

def podatek_2(dochod, zamieszkanie):
    if zamieszkanie in s:
        netto = dochod - (dochod * s[zamieszkanie])
        print(f'Dla miejsca zamieszkania {zamieszkanie}, wypłata netto wynosi {netto}')
    else:
        print('Nie ma takiego miejsca zamieszkania')        

print('------------------')
podatek(35000) 
podatek_2(35000, 'A')
podatek_2(35000, 'D')

