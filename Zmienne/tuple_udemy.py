my_tuple = (1,2,3,4,2,2,1)
# my_tuple[0] = 0
# print(my_tuple) # błąd
print(my_tuple[0]) # 1
print(my_tuple[1]) # 2
print(my_tuple[2]) # 3
print(my_tuple[1:]) # (2, 3, 4, 2, 2, 1)
print('====================')
print(my_tuple.index(1)) # 0
print(my_tuple.index(2)) # 1
print(my_tuple.index(3)) # 2
print(my_tuple.index(4)) # 3
print('===============')
print(my_tuple.count(2)) # 3
print(my_tuple.count(1)) # 2
