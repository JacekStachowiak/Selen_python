l1 = [1,2,3]
l2 = [6,7,8,20,30,40]

for a,b in zip(l1,l2):      # drukujemy pary
    print(a)
    print(b)
print('=========================')
for a,b in zip(l1,l2):      # porównanie
    if a > b:
        print(a)
    else:
        print(b)
print('----------------------')
l4 = [1,2,3]
l5 = [4,5,6,7,8,9]
l6 = [6,7,8,9,77,99]

for a,b,c in zip(l4,l5,l6):
    print(a)
    print(b)
    print(c)