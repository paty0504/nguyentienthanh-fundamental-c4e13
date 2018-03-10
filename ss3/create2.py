menu = ['reading', 'gaming', 'movies']
for index,item in enumerate(menu):
    print(index + 1, '.', item)
position = int(input('Position you want to update '))
# print(menu[position - 1])
menu[position] = input('Change to')
for index, item in enumerate(menu):
    print(index +1, '.', item)
