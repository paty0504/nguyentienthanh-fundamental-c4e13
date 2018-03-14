username = input('Enter your username: ')
count = 0
while count < 3:
    if username == 'tienthanh':
        password = input('Enter your password: ')
        if password == 'thanhnguyen':
            print('Welcome')
            break
        else:
            print('Wrong password!')
    else:
        print('No such user!')

    count += 1
    if count == 3:
        print('You failed to login!')
        break
