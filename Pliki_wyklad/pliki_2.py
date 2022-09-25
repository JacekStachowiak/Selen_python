
my_file = open('trzeci.txt', 'w')
my_file.write('Próbuję coś dopisać')
my_file.close()    

my_file = open('trzeci.txt', 'r')
print(str(my_file.read()))
my_file.close()

# with using - nie musimy zamykać pliku
with open('czwarty.txt', 'w') as f:
    f.write('To jest przykład użycia with')

with open('czwarty.txt', 'r') as f:
    print(str(f.read()))    