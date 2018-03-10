list = [6, 9, 69, 96, 699]
month = 1
while month < 5:

    print('Hey im Thanh and these are my sheep sizes:', list)
    print('Now my biggest sheep has size: ', max(list), '. Lets sheer it!')
    m = max(list)
    for i,j in enumerate(list):
        if j == m:
            list[i] = 8
    print('After sheering it, here is my flock: ', list)
    for i,j in enumerate(list):
        j += 50
        list[i] = j
    print('After a month, now here is my flock: ', list)
    month += 1
s1 = 58
for i in list:
    s1 += i
    size_total = s1 - 58
print('My flock has size in total: ', size_total)
money = size_total*2
print('I would get: ', money, '($)')
