
from random import randint
# n = randint(0, 100)
n = 71
playing = True
count = 0
while playing:
    guess = int(input('Guess my number (0-100)? '))
    if guess > n:
        print('Too big')
    elif guess < n:
        print('Too small')
    else:
        print('bingo')
        break
    count += 1
    if count == 7:
        print('You lose')
        break
