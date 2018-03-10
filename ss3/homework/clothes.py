print('Welcome to our shop! What do you want? Our items:')
menu = ['T-shirt', 'Sweater']
for index,item in enumerate(menu):
    print(index +1, '.', item)
menu.append(input('Enter new item: '))
for index,item in enumerate(menu):
    print(index +1, '.', item)
position = int(input('Update position: '))
menu[position - 1] = input('Change to: ')
for index,item in enumerate(menu):
    print(index +1, '.', item)
fd = int(input('Position to delete': ))
del menu[fd - 1]
for index,item in enumerate(menu):
    print(index +1, '.', item)
