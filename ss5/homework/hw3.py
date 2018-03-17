bac = int(input('How many bacterias? '))
minute = int(input('How much time in minute will we wait? '))
n = minute // 2


for i in range(n):
    bac = bac*2
print('After', minute, 'minutes, we would have: ', bac, 'bacterias')
