number = [1, 6, 2, 2, 1, 8, 2, 6, 9, 3, 9, 1]
#with count()
# num = int(input('Enter a number: '))
# if num in number:
#     print(num, 'appear', number.count(num), 'times in my list')
# else:
#     print('0')

#without count()
num = int(input('Enter a number: '))
count = 0
if num in number:
    for i in number:
        if i == num:
            count += 1
    print(num, 'appears', count, 'times')
else:
    print('0')
