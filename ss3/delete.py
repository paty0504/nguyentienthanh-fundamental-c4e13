favs = ['reading', 'gaming', 'movies']
for index,item in enumerate(favs):
    print(index + 1, '.', item, sep='')
favour = input('Which favour do you want to delete? ')
if favour in favs: #kiem tra xem co nam trong list khong
    favs.remove(favour) #remove by name
else:
    print('Not found')

# position = int(input('Which position do you want to delete? '))
# del favs[position - 1]  #remove by index
for index,item in enumerate(favs):
    print(index + 1, '.', item, sep='')
