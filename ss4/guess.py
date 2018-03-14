print('Guess your number game: \n Now think of a number from 0 to 100, then press Enter: ')
input()
print('All you have to do is to answer to my guess:\n c if my guess is Correct \n s if my guess is smaller than your number \n l if my guess is larger than your number')
low = 0
high = 101

while True:
    mid = (high + low)//2
    # while True:
    #string formating:
    answer = input('Is {0} your number? '.format(mid))
    if answer == 'c':
        print('Right')
        break
    elif answer == 's':
        low = mid
    elif answer == 'l':
        mid = high
    else:
        print('zzz')
