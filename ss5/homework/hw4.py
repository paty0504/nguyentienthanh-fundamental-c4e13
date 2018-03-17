month = 4
n1 = 0
n2 = 1
count = -1
while count < 4:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
    print('Month', count, ':', n3, 'pair(s) of rabbits')
