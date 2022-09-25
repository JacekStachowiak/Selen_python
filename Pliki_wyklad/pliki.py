'''
w - write
r - read
r+ - read and wriate
a - dodaj na końcu
'''
my_list = [1,2,3]
my_file = open('pierwszy.txt', 'w')

for item in my_list:
    my_file.write(str(item) + '\n') # zacznie od nowej linii

my_file.close()    

# czytanie pliku
# read() - czytanie pliku, readline() - czytanie linia po linii

my_file = open('drugi.txt', 'r')
print(str(my_file.read()))
my_file.close()
print('==== Line by line ====')

my_file_line = open('drugi.txt', 'r')
'''
for l in my_file_line.readlines():
    print(str(l), end=' ')
'''
print(str(my_file_line.readline())) # 1 linia
print(str(my_file_line.readline())) # 2 linia
print(str(my_file_line.readline())) # 3 linia
my_file_line.close()

# użycie using with - nie musimy zamykać pliku


