#  stars = int(input('Сколько звезд нужно? '))
#  lines = int(input('Сколько линий нужно? '))
myBlocks = int(input('Сколько блоков звезд нужно? '))

for block in range(1, myBlocks + 1):
    for line in range(1, myBlocks * 2 + 1):
        for star in range(1, (myBlocks + line) * 2 + 1):
            print('⭐️', end='')
        print()
    print()