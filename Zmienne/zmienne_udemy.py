
a = '1abc2abc3abc4abc'
print(a.replace('abc', 'ABC',1)) # 1ABC2abc3abc4abc
a = '1abc2abc3abc4abc'
print(a.replace('abc', 'ABC',2)) # 1ABC2ABC3abc4abc
a = '1abc2abc3abc4abc'
print(a.replace('abc', 'ABC',3))
a = '1abc2abc3abc4abc'
print(a.replace('abc', 'ABC')) # 1ABC2ABC3ABC4ABC

sub = a[1]
print(sub)  # a
sub = a[1:6]
print(sub)  # abc2a
step = a[1:6:1]
print(step) # abc2a
step = a[1:6:2]
print(step) # aca co drugi
step = a[1:6:3]
print(step) #a2
print('===========================')
b = 'To jest przykładowy tekst'
print(b)
print(b[:])
print(b[1:])
print(b[:6])
print(b[-1])
print(b[-2])
print(b[:-1])
print('----------------------')
print(b[:len(b)])
print(b[:len(b)-1])
print(b[:-1])
print('++++++++++++++++++++')
print(b[::])
print(b[::1])
print(b[::2]) # krok co 2
print(b[::-1]) # tsket ywodałkyzrp tsej oT




